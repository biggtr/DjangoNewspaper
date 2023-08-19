from django.shortcuts import render

# Create your views here.


def HomePageView(request):
    if request.method == "GET":
        return render(request, "home.html")
