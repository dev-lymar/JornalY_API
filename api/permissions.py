from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Provides permissions to make edits or deletions only to the author of the object.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
