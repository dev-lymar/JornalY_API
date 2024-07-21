from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """
    A class for creating communities.
    """
    title = models.CharField(max_length=50, verbose_name='Group name', db_index=True)
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Group slug')
    description = models.TextField(verbose_name='Group description')

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    A class for creating tags.
    """
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    A class for creating posts.
    """
    text = models.TextField(verbose_name='Post text')
    pub_date = models.DateTimeField(verbose_name='Date of publication', auto_now_add=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_posts', verbose_name='Author')
    group = models.ForeignKey(
        Group, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Group'
    )
    image = models.ImageField(verbose_name='Image', upload_to='posts/%Y/%m/%d', blank=True)
    tag = models.ManyToManyField(Tag, through='TagPost')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.text[:15] + '...' if len(self.text) > 15 else self.text


class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} {self.post}'


class Comment(models.Model):
    """
    A class for commenting on posts.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment', verbose_name='Comment'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Author')
    text = models.TextField(verbose_name='Comment')
    created = models.DateField(verbose_name='Created', auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    """
    A class for subscribing authors.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', verbose_name='user')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', verbose_name='author')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'], name='unique_followers')
        ]

    def __str__(self):
        return f'{self.user} subscribed to: {self.author}'
