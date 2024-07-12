from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from .models import Photo

# Create your views here.

# def index(request):
#     return HttpResponse('Test Gallery App')

# def index(request):
#     return render(request, 'index.html')

def index(request):
    # return HttpResponse('Temporary Homepage For Gallery App')
    if request.user.is_authenticated:
         photo_list = Photo.objects.all()
         context = {
              'photo_list': photo_list,
         }
         return render(request, 'index.html', context)
    else: 
        return render(request, 'index.html')

# def signup(request):
#      if request.method == 'POST':
#           form = UserCreationForm(request.POST)
#           if form.is_valid():
#                form.save()
#                username = form.cleaned_data.get('username')
#                raw_password = form.cleaned_data.get('password')
#                user = authenticate(username=username, password=raw_password)
#                login(request, user)
#                return redirect(index)
#      else:
#           form = UserCreationForm()
#      return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate the user with the credentials
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                # Handle the case where authentication fails
                return render(request, 'signup.html', {'form': form, 'error': 'Authentication failed. Please try again.'})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class ImageUploadForm(forms.ModelForm):
    class Meta:
         model = Photo
         fields = ('image',)

def upload(request):
     if request.method == 'POST':
          form = ImageUploadForm(request.POST, request.FILES)

          if form.is_valid():
               new_form = form.save(commit=False)
               new_form.author = request.user
               new_form.save()
               return redirect(index)
          else:
               return HttpResponse('Form is not valid')
     else:
          form = ImageUploadForm()
          return render(request, 'upload.html', {'form':form})
     
def custom_logout_view(request):
    logout(request)
    next_page = request.GET.get('next', '/')
    return redirect(next_page)