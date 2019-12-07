from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta
from .models import Profile, BannedIp

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(forms.Form):
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(required=False)

def read_ip(request):
  # We host our server on nginx, so we have to check for the
  # X-Forwarded-For header, otherwise every IP will be 127.0.0.1,
  # which will mark everyone as spam.
  xff = request.META.get('HTTP_X_FORWARDED_FOR')
  if xff:
      return xff.split(',')[0]
  else:
      return request.META.get('REMOTE_ADDR')

def enforce_rate_limit(request, game, user, model):
  """
  Returns `True` if any of the following are true:
  * The user's IP is listed as banned.
  * The user is banned from making posts.
  * The user has already created a review/playthrough/guidebook for this game
  * The user or IP has created more than 10 reviews/playthroughs/guidebooks in the past 15 minutes
  * The user has -5 or fewer karma.

  If `True` is returned, the user will be officially banned from posting, and should be redirected to
  /spam-detected.

  Returns `False` if the user has already made a review/etc. (they are not banned).

  Return None if everything ok.
  """

  ip = read_ip(request)
  now = datetime.now()

  # See if the IP is explicitly banned.
  matching_ips = BannedIp.objects.filter(ip=ip)
  if len(matching_ips) > 0:
    print("ban ip")
    return False

  # Load the user's profile, to check if they are banned.
  profile, _ = Profile.objects.get_or_create(user=user)
  if profile.banned_from_posting:
    return True

  # If they have -5 karma, ban them.
  # They should only be banned from posting, because theoretically, if someone
  # upvotes them, they can be redeemed. However, since their content will be
  # permanently hidden, that is impossible.
  if profile.karma <= -5:
    profile.banned_from_posting = True
    profile.save()
    return True

  # Find any review/playthrough for this game by the user.
  created_by_user = model.objects.filter(author=user, game=game)
  if len(created_by_user) != 0:
    return False

  # Find all reviews by this user  the past 15 minutes.
  # IP tracking
  fifteen_ago = now - timedelta(minutes=15)
  recent_posts = model.objects.filter(
    author=user,
    date_posted__lt=fifteen_ago)

  if len(recent_posts) >= 10:
    # Ban hammer! Spammer detected.
    profile.banned_from_posting = True
    profile.save()
    # Also ban the IP.
    ban_obj = BannedIp.objects.create()
    ban_obj.ip = ip
    ban_obj.save()
    return True

  # All is well.
  return None
