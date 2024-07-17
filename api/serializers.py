from rest_framework import serializers
from posts.models import Post, Group


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        queryset=Group.objects.all(),
        slug_field='slug',
        required=False
    )

    class Meta:
        model = Post
        fields = ('text', 'author', 'image', 'pub_date', 'group')
