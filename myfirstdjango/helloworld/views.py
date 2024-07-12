from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from .models import Post
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User

def index(request):
     
     post_list = Post.objects.all()
     context = {
          'post_list' : post_list,
     }
     return render(request, 'index.html',context)

# def signup(request):
#      if request.method == 'POST':
#           form = UserCreationForm(request.POST)
#           if form.is_valid():
#                form.save()
#                username = form.cleaned_data.get('username')
#                raw_password = form.cleaned_data.get('password')
#                user = authenticate(username=username, password=raw_password)
#                login(request, user)
#                return redirect('index')
#      else:
#           form = UserCreationForm()
#      return render(request, 'signup.html', {'form': form})

def signup(request):
     if request.method == 'POST':
          form = SignUpForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               raw_password = form.cleaned_data.get('password')
               user = authenticate(username=username, password=raw_password)
               login(request, user)
               return redirect('index')
     else:
          form = SignUpForm()
     return render(request, 'signup.html', {'form': form})

class SignUpForm(UserCreationForm):
     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
     Last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
     email = forms.EmailField(max_length=254, help_text='Required. Inform a Valid email address')

     class Meta:
          model = User
          fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')