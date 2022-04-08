from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
import datetime

# Create your views here.

# All POST view methods
def get_post(post_id):
    return Post.objects.get(id=post_id)

def post_list(request):
    posts = Post.objects.order_by('published_date')
    data = { 'all_posts': posts}
    return render(request, 'blog/post_list.html', data)

def post_detail(request, post_id):
    post = get_post(post_id)
    data = { 'post': post}
    return render(request, 'blog/post_detail.html', data)

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.first()
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {
            'form': form,
            'type_of_request': 'New'
        })

def edit_post(request, post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {
            'form': form,
            'type_of_request': 'Edit'
        })

def delete_post(request, post_id):
    post = get_post(post_id)
    post.delete()
    return redirect('post_list')

# All Comment view methods
def comment_list(request, post_id):
    post = get_post(post_id)
    comments = post.comments.all()
    print(comments)
    data = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/comment_list.html', data)

def comment_detail(request, post_id, comment_id):
    post = get_post(post_id)
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'blog/comment_detail.html', {'post': post, 'comment': comment})

def new_comment(request, post_id):
    post = get_post(post_id)
    author = User.objects.get(username='chad')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('comment_detail', post_id=post.id, comment_id=comment.id)
        print(request)
    else:
        form = CommentForm({'post': post, 'comment_author': author})
        return render(request, 'blog/comment_form.html', {
            'form': form,
            'type_of_request': 'New'
        })

def edit_comment(request, post_id, comment_id):
    post = get_post(post_id)
    comment = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('comment_detail', post_id=post.id, comment_id=comment.id)
        print(request)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'blog/comment_form.html', {
            'form': form,
            'type_of_request': 'Edit'
        })

def delete_comment(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('comment_list', post_id=post_id)

def all_comments(request):
    all_comments = Comment.objects.all()
    data = {
        'comments': all_comments
    }
    return render(request, 'blog/comment_list.html', data)

def write_new_comment(request):
    author = User.objects.get(username='chad')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('comment_detail', post_id=comment.post.id, comment_id=comment.id)
        # do something
        print(request)
    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', {
            'form': form,
            'type_of_request': 'New'
        })
