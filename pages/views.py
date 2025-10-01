from django.shortcuts import render

def home_view(request):
    return render(request, "pages/home.html")

def about_view(request):
    return render(request, "pages/about.html")

def hello_view(request):
    return render(request, "pages/hello.html")

from django.shortcuts import render

def about_view(request):
    context = {
        "name": "Lyken J. Suarez",
        "student_id": "2023-11929",
    }
    return render(request, "pages/about.html", context)

def home_view(request):
    context = {
        "course": "IT373 - Web Systems and Technologies 2",
        "week": "1",
    }
    return render(request, "pages/home.html", context)

