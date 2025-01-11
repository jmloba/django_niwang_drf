

from django.core.exceptions import PermissionDenied

class CheckPremiumGroupMixin():
  def dispatch(self, request, permission,* args, **kwargs):

    if request.user.groups.filter(name="default").exists():
    # if request.user.permission.filter(codename=permission).exists():  
      print(f'default exists : mixin dispath module ')
      
      return super().dispatch(request, *args, **kwargs)
    else:
      raise PermissionDenied

