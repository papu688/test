from django.shortcuts import render, redirect

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        return redirect('allgood')
    return render(request, 'portfolio/contact.html')


def allgood_view(request):
    return render(request, 'portfolio/allgood.html')

def project_view(request):
    projects = [
        {'name': 'Todo app', 'description': 'the coolest todo web application in the world'},
        {'name': 'Facebook app', 'description': 'Facebook Clone, thats....'},
        {'name': 'Facebook app', 'description': 'Facebook Clone, thats....'},
        {'name': 'Facebook app', 'description': 'Facebook Clone, thats....'},
        {'name': 'Facebook app', 'description': 'Facebook Clone, thats....'},
        {'name': 'Facebook app', 'description': 'Facebook Clone, thats....'}
    ]
    return render(request, 'portfolio/projects.html', {'projects': projects})

