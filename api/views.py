from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from .throttling import EarlyMorningThrottle


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Post model objects.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    throttle_classes = (EarlyMorningThrottle,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$text',)

    def perform_create(self, serializer):
        """
        Creates a post where the current user is the author.
        """
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Group model objects.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Comment model objects.
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_post(self):
        """
        Returns the object of the current post.
        """
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        """
        Returns a queryset with comments for the current post.
        """
        return Comment.objects.filter(post=self.get_post())

    def perform_create(self, serializer):
        """
        Creates a comment for the current post, where the author is the current user.
        """
        serializer.save(
            author=self.request.user,
            post=self.get_post(),
        )
