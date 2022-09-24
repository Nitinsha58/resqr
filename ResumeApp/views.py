from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .decorators import unauthenticated_user
from .forms import UserAuthenticationForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from .models import PersonalInfo

# Create your views here.
def index(request):

    context = {}
    return render(request, 'ResumeApp/index.html', context)

@unauthenticated_user
def loginPage(request):

    form = UserAuthenticationForm()
    error_msg = None
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # messages.success(request, 'You logged in Successfully.')
            login(request, form.user_cache)
            return redirect('home')
        else:
            # messages.error(request, 'Invalid Username or Password')
            error_msg = 'Invalid Username or password'
            redirect('dashboard')

    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'login.html', context)

@unauthenticated_user
def registerPage(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'{username}, Account is created for you. ')
            return redirect('login-user')
        else:
            # messages.success(request, 'Please enter valid details.')
            context = {'form': form}
            return render(request, 'register.html', context)
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'register.html', context)

login_required('login-user')
def logoutPage(request):
    logout(request)
    return redirect('home');
    

login_required('login-user')
def dashboard(request):
    resumes = PersonalInfo.objects.filter(user = request.user)
    context = {'resumes': resumes}
    return render(request, 'ResumeApp/dashboard.html', context);