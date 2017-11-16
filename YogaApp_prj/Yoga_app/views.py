from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from django.utils import timezone
from Yoga_app.models import Contact
from Yoga_app.models import Post
from Yoga_app.forms import BlogPostForm

def say_yoga(request):
	position = 'Downward Dog'
	html = '<html><body><h1>Yoga %s!</h1></body></html>' % position
	return HttpResponse(html)

def get_now(request):
	now = datetime.datetime.now()
	return render(request, "Yoga/base.html", {"current_date": now})

def get_contacts(request):
    return render(request, "Yoga/home.html",
                  {'contact_list': Contact.objects.all()})

def timetable_page(request):
    return render(request, "Yoga/timetable.html",
                  {"b_variable": "Class Timetable",
                   "other_variable": "Winter class timetable, for private lessons, please visit the contact page."})

def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "Yoga/templates/poseblog.html", {'posts': posts})

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