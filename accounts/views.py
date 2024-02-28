from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from .forms import SignUpForm
from .models import UserProfile
from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile
import random
from .send_email import email_sending
# Create your views here.


def user_login(request):
    '''Log the user into the system'''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Login Credentials')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('accounts:login')


# def signup(request):
#     if request.method == 'POST':

#         form = SignUpForm(request.POST)
#         raw_password = request.POST['password1']
#         password2 = request.POST['password2']

#         if raw_password != password2:
#             messages.error(request, 'Passwords do not match')
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             raw_password = form.cleaned_data['password1']

#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')

#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            profile, created = Profile.objects.get_or_create(user=user)
            profile.otp = random.randint(100000, 999999)
            profile.save()

            # send_mail(
            #     'Verify your account',
            #     f'Your OTP for account verification is: {profile.otp}',
            #     'kundancoder1@gmail.com',
            #     [user.email],
            #     fail_silently=False,
            # )
            email_sending(user.email, str(profile.otp))

            # return redirect('verify_otp', user_id=user.id)
            return redirect('accounts:verify_otp', user_id=user.id)
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

def verify_otp(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        if int(otp_entered) == profile.otp:
            user.is_active = True
            user.save()
            return redirect('accounts:login')  # Assuming you have a login view
        else:
            return render(request, 'accounts/verify_otp.html', {'error': 'Invalid OTP', 'user_id': user_id})

    return render(request, 'accounts/verify_otp.html', {'user_id': user_id})

def forgotpassword(request):
    return render(request, "accounts/forgot-password.html")