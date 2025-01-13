from django.shortcuts import render, redirect
from app_blog.models import BlogPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User,Group,Permission


# Create your views here.
@login_required(login_url='accounts:login-view')
@permission_required("app_blog.view_post",login_url='home', raise_exception=True)
def postDashboard(request):

  data=BlogPost.objects.all()
  form = PostForm
  if request.method=='POST':
    post_id = request.POST.get('post-id')
    user_id = request.POST.get('user-id')
    if post_id:
      post = BlogPost.objects.filter(id=post_id).first()
      if post and (post.author == request.user or request.user.has_perm('app_blog.delete_post')):
        post.delete()
      return redirect('app_blog:postDashboard')
    elif user_id:
      user = User.objects.filter(id=user_id).first()
      print(f'user to ban: {user}')
      if user and request.user.is_staff:
        # remove user from default group - permision add and view
        try:
          group = Group.objects.get(name='default') 
          group.user_set.remove(user)
        except :
          pass

        try:  
          group = Group.objects.get(name='mod') 
          group.user_set.remove(user)
        except:
          pass






  
  context={"data":data, 'form': form }
  return render(request,'app_blog/dashboard-post.html', context)

@login_required(login_url='accounts:login-view')
def CreatePost(request):
  if request.method=='POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)  
      post.author = request.user
      post.save()
      return redirect('app_blog:postDashboard')
  


    
