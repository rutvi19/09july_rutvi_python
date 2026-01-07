from django.shortcuts import render, get_object_or_404,redirect
from user .models import userlogin,post 


# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def all_posts(request):
    posts = post.objects.all()
    return render(request,'posts.html',{'posts': posts})

def users_list(request):
    users = userlogin.objects.all() 
    return render(request,'users.html', {'users': users})

def detail_post(request, id):
   
    post = get_object_or_404(post, id=id) 
    
   
    return render(request, 'detail.html', {'post': post})

def delete_user(request, id):
    
    user_obj = get_object_or_404(userlogin, id=id) 
    
   
    user_obj.delete()
    
    
    return redirect('manage_users')