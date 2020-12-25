from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import BlogPostForm


# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    uname = request.POST.get('uname')
    passwd = request.POST.get('passwd')

    user = auth.authenticate(request, username=uname, password=passwd)

    if not user:
        messages.error(request, 'Error logging in: Invalid username or password.')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Successfully logged in.')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    messages.warning(request, 'You have logged out.')
    return redirect('login')


def register(request):
    if request.method != 'POST':
        # messages.info(request, 'Nothing sent.')
        return render(request, 'register.html')

    print(request.POST)
    uname = request.POST.get('uname')
    email = request.POST.get('email')
    passwd_1 = request.POST.get('passwd_1')
    passwd_2 = request.POST.get('passwd_2')

    if not uname or not email or not passwd_1 or not passwd_2:
        messages.error(request, 'All fields must be filled.')
        return render(request, 'register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail not valid.')
        return render(request, 'register.html')

    if passwd_1 != passwd_2:
        messages.error(request, 'Passwords do not match.')
        return render(request, 'register.html')

    if User.objects.filter(username=uname).exists():
        messages.error(request, 'Username already exists.')
        return render(request, 'register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail already registered.')
        return render(request, 'register.html')

    user = User.objects.create_user(username=uname, email=email, password=passwd_1)
    user.save()
    messages.success(request, 'Successfully registered.')
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = BlogPostForm()
        return render(request, 'dashboard.html', {'form': form})
    else:
        form = BlogPostForm(request.POST, request.FILES)

        if not form.is_valid():
            messages.error(request, 'Error validating form.')
            form = BlogPostForm(request.POST)
            return render(request, 'dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Blog post {request.POST.get("title")} created successfully.')
    return redirect('dashboard')
