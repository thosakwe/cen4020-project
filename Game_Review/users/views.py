from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Profile
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
import os

# Create your views here.


def register(request):
    captcha = ReCaptchaField()
    if request.method == 'POST':
        # if we get a POST request, create a user creation
        # form
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            ReCaptchaField()
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Go ahead and login')
            return redirect('login')
    else:
        # else, create an empty form
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'recaptcha3': captcha, })


@login_required
def profile(request):
    # Fetch the user's profile.
    errors = []
    user_id = int(request.GET.get('user_id', request.user.id))
    # TODO: If the user does not exist, display a 404 page.
    the_user = User.objects.get(pk=user_id)
    profile, _ = Profile.objects.get_or_create(user=the_user)

    if request.method == "POST":
        if the_user.id != request.user.id:
            errors.extend(["You can only edit your own profile."])
        else:
            form = EditProfileForm(request.POST, request.FILES)
            if form.is_valid():
                avatar = form.cleaned_data['avatar']
                bio = form.cleaned_data['bio']

                # If the user uploaded an avatar, save it.
                # Validate image sizes, mime types, etc.
                if avatar:
                    if avatar.content_type != "image/jpeg":
                        errors.extend(
                            ["Profile pictures must be jPEG images."])
                    else:
                        # dirname = os.path.dirname(os.path.abspath(__file__))
                        dirname = os.path.dirname(__file__)
                        review_path = os.path.join(dirname, "..", "review")
                        avatars_path = os.path.join(review_path, "static", "avatars")
                        file_path = os.path.join(avatars_path, str(the_user.id) + ".jpg")
                        avatar_dir = os.path.dirname(file_path)
                        if not os.path.exists(avatar_dir):
                            os.makedirs(avatar_dir)
                        with open(file_path, "wb") as file:
                            for chunk in avatar.chunks():
                                file.write(chunk)
                        # Update the user's profile.
                        profile.avatar = "/static/avatars/" + str(the_user.id) + ".jpg"
                profile.bio = bio or profile.bio
                profile.save()
            else:
                errors = form.errors
    return render(request, 'users/profile.html', {'errors': errors, 'profile': profile, 'the_user': the_user})
