from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect


from .forms import MaullidoForm
from .models import Maullido

def home(request):
    maullidos = Maullido.objects.all().order_by('-fecha')
    return render(request, 'home.html', {'maullidos': maullidos})

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def post_maullido(request):
    """Post a new maullido."""
    if request.method == 'POST':
        form = MaullidoForm(request.POST)
 
        if form.is_valid():
            maullido = form.save(commit=False)
            maullido.usuario = request.user
            maullido.save()
            return redirect('user_page', username=request.user.username)
    else:
        form = MaullidoForm()
    return render(request, 'maullidos/post_maullido.html', {'form': form})

def user_page(request, username):
    """Show a user's page."""
    user = get_object_or_404(User, username=username)
    maullidos = Maullido.objects.filter(usuario=user).order_by('-fecha')
    return render(request, 'maullidos/user_page.html', {'user_profile': user, 'maullidos': maullidos})
