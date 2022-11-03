from rest_framework import permissions

class IsAuthenticatedForSafe(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticaed or request.method in permissions.SAFE_METHODS

class IsStaffOrOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):


        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_staff or request.user == obj.owner 

