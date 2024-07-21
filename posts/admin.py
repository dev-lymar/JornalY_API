from django.contrib import admin

from .models import Comment, Follow, Group, Post

admin.site.site_title = 'Admin panel JornalY API'
admin.site.site_header = 'Admin panel JornalY API'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post Section Configuration Class.
    """

    list_display = (
        'pk',
        'text',
        'image',
        'pub_date',
        'author',
        'group',
        'count_comments',
    )
    empty_value_display = '-empty-'
    list_editable = ('group',)
    list_filter = ('pub_date',)
    list_per_page = 10
    search_fields = ('text',)

    def count_comments(self, object):
        return object.comment.count()

    count_comments.short_description = 'Number of comments'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    Group Section Configuration Class.
    """

    list_display = (
        'pk',
        'title',
        'slug',
        'description',
        'count_posts'
    )
    empty_value_display = '-empty-'
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def count_posts(self, object):
        return object.posts.count()

    count_posts.short_description = 'Number of posts'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment Section Configuration Class.
    """

    list_display = (
        'pk',
        'post',
        'author',
        'text',
        'created'
    )

    list_editable = ('author',)
    list_filter = ('author',)
    list_per_page = 10
    search_fields = ('text',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """
    Follow Section Configuration Class.
    """

    list_display = (
        'pk',
        'author',
        'user',
    )

    list_editable = ('author',)
    list_filter = ('author',)
    list_per_page = 10
    search_fields = ('author',)
