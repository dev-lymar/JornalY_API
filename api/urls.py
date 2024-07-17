from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
