from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Blog
from .forms import BlogCreationForm, BlogUpdateForm
from django.contrib.auth.decorators import login_required


def index(request):
    """ Home page """
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog/index.html', {'blogs':blogs})

@login_required(login_url='accounts:login')
def detail(request, blog_id):
    """ Get a specific blog """
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})

@login_required(login_url='accounts:login')
def list(request):
    """ List of user blogs """
    blogs = Blog.objects.filter(author=request.user).order_by('-published_date')
    return render(request, 'blog/list.html', {'blogs':blogs})

@login_required(login_url='accounts:login')
def create(request):
    """ Create a new blog """
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            blog = Blog.objects.create(
                author=request.user,
                title=data['title'],
                text=data['text'],
            )
            if blog:
                blog.save()
                messages.success(request, "Blog created successfully.")
                return redirect('blog:list')
            
            else:
                messages.error(request, "There is an error.", 'danger')
                
        return render(request, 'blog/create.html', {'form':form})
    
    else:
        form = BlogCreationForm
        return render(request, 'blog/create.html', {'form':form})

@login_required(login_url='accounts:login')
def update(request, blog_id):
    """ Modify the blog """
    blog = Blog.objects.get(pk=blog_id)
    if request.user != blog.author:
        messages.error(request, "You don't have permission to delete this blog.", 'danger')
        return redirect('blog:index')
    
    if request.method == 'POST':
        form = BlogUpdateForm(request.POST, instance=blog)
        if form.is_valid():
            data = form.cleaned_data
            if blog.author == request.user:
                 blog.title = data['title']
                 blog.text = data['text']
                 blog.save()
                 messages.success(request, f'{blog.title} updated successfully. ')
                 return redirect('blog:list')
             
            else:
                messages.error(request, 'You are not allowed do edit this blog. ', 'danger')
                
        return render(request, 'blog/update.html', {'form':form})
    
    else:
        form = BlogUpdateForm(instance=blog)
        return render(request, 'blog/update.html', {'form':form})

@login_required(login_url='accounts:login')
def delete(request, blog_id):
    """ Redirect the user to another page to confirm the deletion """
    blog = Blog.objects.get(pk=blog_id)
    if request.user == blog.author:
        title = blog.title
        request.session['confirm'] = {
            'pk':blog_id,
            'title':title,
        }
        return redirect('blog:confirm')
    
    else:
        messages.error(request, "You don't have permission to delete this blog.", 'danger')
        return redirect('blog:index')

@login_required(login_url='accounts:login')
def confirm_delete(request):
    """ Delete a blog after user confirmation """
     # If the user comes from another page, it raises a key validation error, so we don't allow the user to access this page.
    try:
        data = request.session['confirm']
    except:
        messages.error(request, "You don't have access to this page. ", 'danger')
        return redirect('blog:index')
    
    title = data['title']
    if request.method == 'POST':
        if request.POST.get('confirm') == 'Yes':
            blog = Blog.objects.get(pk=data['pk'])
            blog.delete()
            messages.success(request, 'Blog deleted successfully.')
            del request.session['confirm']
            return redirect('blog:list')
        
        elif request.POST.get('confirm') == 'Cancel':
            return redirect('blog:list')

    return render(request, 'blog/confirm.html', {'title':title})
