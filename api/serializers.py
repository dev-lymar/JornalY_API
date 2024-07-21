from rest_framework import serializers
from posts.models import Post, Group, Tag, TagPost, Comment


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tag model.
    """
    class Meta:
        model = Tag
        fields = ('name', )


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    group = serializers.SlugRelatedField(
        queryset=Group.objects.all(),
        slug_field='slug',
        required=False
    )
    tag = TagSerializer(many=True, required=False)
    character_quantity = serializers.SerializerMethodField()
    publication_date = serializers.DateTimeField(source='pub_date', read_only=True)

    class Meta:
        model = Post
        fields = ('text', 'author', 'image', 'publication_date', 'group', 'tag', 'character_quantity')
        read_only_fields = ('author',)

    def create(self, validated_data):
        if 'tag' not in validated_data:
            post = Post.objects.create(**validated_data)
            return post

        tags = validated_data.pop('tag')
        post = Post.objects.create(**validated_data)

        for tag in tags:
            current_tag, status = Tag.objects.get_or_create(**tag)
            TagPost.objects.create(tag=current_tag, post=post)

        return post

    def get_character_quantity(self, obj):
        return len(obj.text)


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model.
    """
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('post',)
