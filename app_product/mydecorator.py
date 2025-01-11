

from django.shortcuts import render
import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

decorator_with_arguments = lambda decorator: lambda *args, **kwargs: lambda func: decorator(func, *args, **kwargs)
print(f'\n\n decorator_with_arguments : {decorator_with_arguments}  ')


def group_required(group,login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group,)
        else:    
            groups = (group,)
        # first check if the user has permission
        if user.groups.filter(name=groups).exists():
            return True
        # in case 403 handler
        if raise_exception:
            raise PermissionDenied
        # as last resort , show the login form
        return False
    
    return user_passes_test(check_perms, login_url=login_url)

    


@decorator_with_arguments
def custom_permission_required(function, perm):
    def _function(request, *args, **kwargs):
        if request.user.has_perm(perm):
            print(f'**** has permission  ***')
            return function(request, *args, **kwargs)
        else:
            print(f'**** no  permission  !!! ***')
            template='include/no_permission.html' 
            context={}
            return render(request, template,context)
    return _function