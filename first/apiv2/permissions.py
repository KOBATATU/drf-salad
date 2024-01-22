from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):

    # message = 'Adding customers not allowed.'
    def has_permission(self, request, view):
        print(request.user.id)
        print(dir(view))
        return True