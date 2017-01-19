from django.shortcuts import render, redirect

def home(request):
    return render(request, 'talkapp/home.html')


def user_create(request):
    return render(request, 'talkapp/user_create.html')

def user_store(request):
    return redirect('post_index')

def user_edit(request):
    return render(request, 'talkapp/user_edit.html')

def user_update(request):
    return redirect('post_index')


class Post:
    def __init__(self):
        self.message = ""

def post_index(request):
    post1 = Post()
    post1.message = "Message 1"
    post2 = Post()
    post2.message = "Message 2"
    post3 = Post()
    post3.message = "Message 3"
    posts = [post1, post2, post3]
    context = {
        'posts' : posts
    }
    return render(request, 'talkapp/post_index.html', context)

def post_create(request):
    return render(request, 'talkapp/post_create.html')

def post_store(request):
    return redirect('post_index')

def post_delete_all(request):
    return redirect('post_index')


def getLogin(request):
    return render(request, 'talkapp/getlogin.html')

def postLogin(request):
    return redirect('post_index')

def getLogout(request):
    return render(request, 'talkapp/home.html')
