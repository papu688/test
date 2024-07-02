from django.shortcuts import render

def blog_view(request):
    blog_title = ['Blog post 1', 'Blog post 2', 'Blog post 3']

    data = {'blog_names': blog_title}

    return render(request, 'blog/index.html', data)
