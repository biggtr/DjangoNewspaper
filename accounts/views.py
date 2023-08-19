from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("login"))

    else:
        form = CustomUserCreationForm()
        return render(request, "registration/signup.html", {"form": form})
