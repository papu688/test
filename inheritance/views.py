from django.shortcuts import render, redirect

# Create your views here.

def inheritance_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        return redirect('main')
    return render(request, 'contact.html')

def main_view(request):
    return render(request, 'index.html')
