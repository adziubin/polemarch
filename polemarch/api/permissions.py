from rest_framework import permissions


class ModelPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super(ModelPermission, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj:
            return True
        if request.method in permissions.SAFE_METHODS:  # nocv
            return obj.acl_handler.viewable_by(request.user)  # nocv
        if view.action in view.POST_WHITE_LIST:  # nocv
            return obj.acl_handler.viewable_by(request.user)  # nocv
        return obj.acl_handler.editable_by(request.user)  # noce
