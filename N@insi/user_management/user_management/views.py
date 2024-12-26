from django.http import HttpResponse

def index(request):
    return HttpResponse("welcome to views.py")

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserForm

def list_users(request):
    users = User.objects.all()  # Fetch all users, including the `role` field
    return render(request, 'list_users.html', {'users': users})
def hello(request):
    return render(request, 'hello.html')

# View to display details of a specific user by ID
# def user_detail(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     return render(request, 'user_detail.html', {'user': user})
from django.shortcuts import render
from .models import User


def search_user(request):
    user = None
    error_message = None

    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                error_message = f"No user found with ID {user_id}."
        else:
            error_message = "Please provide a valid user ID."

    return render(request, 'user_detail.html', {'user': user, 'error_message': error_message})

# View to display a specific user's details

def user_detail(request, user_id=None):
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None
    else:
        # Handle the case where no user_id is provided (e.g., default user)
        user = User.objects.first()  # Example: Get the first user

    return render(request, 'user_detail.html', {'user': user})

# View to display all users
def AllUsers(request):
    users = User.objects.all()
    return render(request, 'AllUser.html', {'users': users})


# View for the homepage
def index(request):
    return render(request, 'index.html')


# View to handle adding a new user
  # Replace with your form class if defined

def new_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        role = request.POST.get("role")

        # Create a new user and save it to the database
        user = User(name=name, email=email, role=role)
        user.save()

        return redirect('user_list')
    return render(request, 'new_user.html')


# View to display and manage users
def user_detail(request, user_id=None):
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None
    else:
        user = User.objects.first()  # Or handle the case where no user_id is given

    return render(request, 'user_detail.html', {'user': user})
def user_list(request):
    users = User.objects.all()  # Make sure you're getting the users from the database
    return render(request, 'user_list.html', {'users': users})