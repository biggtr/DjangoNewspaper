from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            if CustomUser.objects.filter(email=email).exists():
                form.add_error("email", "This email address is already registered.")
            else:
                user = form.save()
                login(request, user)
                return redirect(reverse_lazy("home"))

    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
