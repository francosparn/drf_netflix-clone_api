from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allows administrators to perform all actions
        return request.user.is_staff


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allows authenticated users to perform read actions
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        
        # Reject access to unauthenticated users and authenticated users for write actions
        return False