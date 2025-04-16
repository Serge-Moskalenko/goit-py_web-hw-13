from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


