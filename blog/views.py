from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def projects(request):
    return render(request, 'blog/projects.html')

def skills(request):
    return render(request, 'blog/skills.html')

def contact(request):
    return render(request, 'blog/contact.html')
