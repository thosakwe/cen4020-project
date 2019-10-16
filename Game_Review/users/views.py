from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, UserRegistrationForm
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Profile
import os

# Create your views here.


def register(request):
    if request.method == 'POST':
        # if we get a POST request, create a user creation
        # form
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Go ahead and login')
            return redirect('login')

    else:
        # else, create an empty form
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # Fetch the user's profile.
    profile, _ = Profile.objects.get_or_create(user=request.user)
    errors = []

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            bio = form.cleaned_data['bio']

            # If the user uploaded an avatar, save it.
            # Validate image sizes, mime types, etc.
            if avatar:
                if avatar.content_type != "image/jpeg":
                    errors.extend(["Profile pictures must be jPEG images."])
                else:
                    file_path = "review/static/avatars/" + str(request.user.id) + ".jpg"
                    avatar_dir = os.path.dirname(file_path)
                    if not os.path.exists(avatar_dir):
                        os.makedirs(avatar_dir)
                    with open(file_path, "wb") as file:
                        for chunk in avatar.chunks():
                            file.write(chunk)

            # Update the user's profile.
            profile.avatar_path = "/static/avatars/" + str(request.user.id) + ".jpg"
            profile.bio = bio or profile.bio
            profile.save()
        else:
            errors = form.errors
    return render(request, 'users/profile.html', {'errors': errors, 'profile': profile})
