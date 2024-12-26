from django.contrib import messages
from django.shortcuts import render, redirect
from user_management.user_management.models import User


# View to display details of a specific user by ID
def user_detail(request):
    user = User.objects.all()  # Ensure User refers to the correct model
    return render(request, 'user_detail.html', {'users': user})



# View to display all users
def AllUsers(request):
    users = User.objects.all()
    return render(request, 'AllUsers.html', {'users': users})
def list_users(request):
    users = User.objects.all()  # Fetch all users from the database
    return render(request, 'list_users.html', {'users': users})

# View for the homepage
def index(request):
    return render(request, 'index.html')


# View to handle adding a new user
def new_user(request):
    def add_user(request):
        if request.method == "POST":
            # Get data from the form
            name = request.POST.get('name')
            email = request.POST.get('email')
            role = request.POST.get('role')

            # Create a new user object and save it to the database
            user = User(name=name, email=email, role=role)
            user.save()

            # After saving, redirect to the users list page
            return redirect('user_list')  # Make sure 'user_list' is the name of your user list URL

        return render(request, 'new_user.html')  # Render the form if it's a GET request


# View to display and manage users
def users(request):
    if request.method == "POST":
        # Form submission handled in `add_user` view
        return redirect('new_user')

    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
def user_list(request):
    # Retrieve all users from the database
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})