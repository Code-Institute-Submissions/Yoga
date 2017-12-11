from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from django.utils import timezone
from Yoga_app.models import Contact
from Yoga_app.models import Post
from Yoga_app.forms import BlogPostForm

def get_index(request):
    return render(request, 'Yoga/templates/index.html')

def go_home(request):
    return render(request, "Yoga/home.html")

def timetable_page(request):
    return render(request, "Yoga/templates/timetable.html")

def price_list(request):
    return render(request, "Yoga/templates/prices.html", )

def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "Yoga/templates/blog.html", {'posts': posts})

def post_detail(request, id):

    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "Yoga/templates/postdetail.html", {'post': post})

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'Yoga/templates/blogpostform.html', {'form': form})

def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'Yoga/templates/blogpostform.html', {'form': form})