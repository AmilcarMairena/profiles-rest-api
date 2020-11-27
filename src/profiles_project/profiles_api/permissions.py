from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow to user to update ther own status."""

    def has_object_permission(self,request,view,obj):
        """Check the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return Truex

        return obj.user_profile.id == request.user.id
