from rest_framework.permissions import BasePermission


class IsHR(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            'view_candidates' in request.user.permissions
        )


class IsHROrAccounts(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            'edit_penalties' in request.user.permissions
        )


class IsHROrAccountsOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            'view_penalties' in request.user.permissions
        )


class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            'view_staff' in request.user.permissions
        )

