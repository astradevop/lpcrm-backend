from rest_framework.permissions import BasePermission


class IsManagement(BasePermission):
    """
    Management-level users who can view staff lists and details
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            'view_staff' in request.user.permissions
        )


class IsSuperAdmin(BasePermission):
    """
    Very restricted actions like deleting staff
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            'view_staff' in request.user.permissions and 
            'edit_tasks' in request.user.permissions
        )


def HasPermission(required_permission):
    """
    Factory function returning a BasePermission class that checks
    if the user's permissions JSONField contains the required string.
    """
    class _HasPermission(BasePermission):
        def has_permission(self, request, view):
            if not request.user.is_authenticated:
                return False
            
            # If the user is an admin or CEO, maybe they have blanket access, 
            # but for now we strictly check the permissions list.
            perms = request.user.permissions or []
            return required_permission in perms

    return _HasPermission
