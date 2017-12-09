from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        user_npm = request.user.npm
        user_npm_on_url = request.resolver_match.kwargs.get('pk', None)
        return user_npm == user_npm_on_url