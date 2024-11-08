from django.shortcuts import render
from .models import Room,Message
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm,RoomForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "You are registered.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'chatapp/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('rooms')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'chatapp/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('rooms')


def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form = RoomForm()
    return render(request, 'chatapp/create_room.html', {'form': form})

def rooms(request):
    rooms=Room.objects.all()
    return render(request, "rooms.html",{"rooms":rooms})

def room(request, slug):
    room_instance = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room_instance).order_by("created_on")  # Orders messages by timestamp
    return render(request, "room.html", {"room_name": room_instance.name, "slug": slug, 'messages': messages})

