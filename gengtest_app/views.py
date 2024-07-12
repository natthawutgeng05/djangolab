from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import Post

# Create your views here.
def index(request):
     
     post_list = Post.objects.all()
     context = {
          'post_list' : post_list,
     }
     return render(request, 'index.html',context)


# def index(request):
#     return HttpResponse("")

def signup(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               raw_password = form.cleaned_data.get('password')
               user = authenticate(username=username, password=raw_password)
               login(request, user)
               return redirect('index')
     else:
          form = UserCreationForm()
     return render(request, 'signup.html', {'form': form})