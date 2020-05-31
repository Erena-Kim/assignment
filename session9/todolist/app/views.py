from django.shortcuts import render, redirect
from .models import Post, Comment
#이미 만들어진 User model import해서 사용하기
from django.contrib.auth.models import User
#회원가입과 동시에 로그인시키기
from django.contrib import auth
#권한 부여하기
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.order_by('duedate')
    return render(request, 'home.html', {'posts' : posts})

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        Comment.objects.create(
            post = post,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', post_pk)
    return render(request, 'detail.html', {'post' : post})

@login_required(login_url = '/registration/login')
def new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate'],
            author= request.user
        )
        return redirect('detail', new_post.pk)
    else:
        return render(request, 'new.html')

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate']
        )
        return redirect('detail', post_pk)
    else:
        return render(request, 'edit.html', {'post' : post})

def delete(request, post_pk):
    Post.objects.get(pk=post_pk).delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('detail', post_pk)

def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        #오류처리
        if len(found_user) > 0:
            error = "User name이 이미 존재합니다"
            return render(request, 'registration/signup.html', {'error':error})
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        #회원가입과 동시에 로그인시키기
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend' ) #유저를 만들고 나서 
        return redirect('home')
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = "아이디 또는 비밀번호가 틀렸습니다"
            return render(request, 'registration/login.html', {'error':error})
        auth.login(request, found_user, backend='django.contrib.auth.backends.ModelBackend' )
        return redirect(request.GET.get('next','/')) #이게 무슨 의민지 모르겟움 ㅠㅠ
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url = '/registration/login')
def mypage(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'mypage.html', {'posts' : posts}) 