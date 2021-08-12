from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm, BlogForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	template = "index.html"
	posts = Post.objects.all().order_by('-created_on')
	context = {
		"posts": posts,
	}
	return render(request, template, context)

def add_blog(request):
	template = "add_blog.html"
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'blog_form': BlogForm(),
		}
	return render(request, template, context)

def update_blog(request, blog_id):
	template = "update_blog.html"
	post = Post.objects.get(id=int(blog_id))
	if request.method == "POST":
		form = BlogForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'blog_form': BlogForm(instance=post),
		}

	return render(request, template, context)

def view_blog(request, blog_id):
	template = "view_blog.html"
	post = Post.objects.get(id=blog_id)

	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				author=form.cleaned_data["author"],
				body=form.cleaned_data["body"],
				post=post
			)
			comment.save()

	comments = Comment.objects.filter(post=post)
	context = {
		"post": post,
		"comments": comments,
		"form": form,
	}

	return render(request, template, context)

def delete_comment(request, comment_id):
	comment = Comment.objects.get(id=int(comment_id))
	comment.delete()
	return HttpResponseRedirect(reverse_lazy('blog:index'))
