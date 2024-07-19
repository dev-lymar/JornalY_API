from rest_framework import viewsets
from rest_framework import filters

from posts.models import Post
from .serializers import PostSerializer
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
