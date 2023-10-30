from django.shortcuts import redirect, render
# from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model

from user.forms import UserForm
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
User = get_user_model()


def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    context = {
        'form': form,
    }
    return render(request, "user/signup.html", context)