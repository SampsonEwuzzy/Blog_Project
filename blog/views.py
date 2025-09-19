from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Post, Category, Comment, Like
from .forms import PostForm, CommentForm

def get_base_context(request):
    """Helper function to get context needed for all views."""
    categories = Category.objects.all().order_by('name')
    return {'categories': categories}

def post_list(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    
    # Get the 6 most recent posts for the carousel
    latest_posts = posts[:6]

    context = {
        "posts": posts,
        "latest_posts": latest_posts,
    }
    context.update(get_base_context(request))
    return render(request, "blog/post_list.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    comments = post.comments.all()
    
    # Handle comment submission
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post-detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    # Pass like and comment data to the template
    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        "total_likes": post.likes.count(),
        "is_liked": post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
    }
    context.update(get_base_context(request))
    return render(request, "blog/post_detail.html", context)

@login_required
def post_create(request):
    """Allows authenticated users to create a new post."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post-detail', slug=new_post.slug)
    else:
        form = PostForm()
    
    context = {"form": form}
    context.update(get_base_context(request))
    return render(request, "blog/post_form.html", context)

@login_required
def post_update(request, slug):
    """Allows a post's author to update their own post."""
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    context = {"form": form}
    context.update(get_base_context(request))
    return render(request, "blog/post_form.html", context)

@login_required
def post_delete(request, slug):
    """Allows a post's author to delete their own post."""
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect('post-list')
    
    context = {"post": post}
    context.update(get_base_context(request))
    return render(request, "blog/post_confirm_delete.html", context)

@login_required
def posts_by_category(request, category_slug):
    """Displays posts filtered by category."""
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status="published").order_by("-created_at")

    context = {"category": category, "posts": posts}
    context.update(get_base_context(request))
    return render(request, "blog/category_posts.html", context)

@login_required
@require_POST
def like_post(request, slug):
    """View to handle liking and unliking a post."""
    post = get_object_or_404(Post, slug=slug)
    user = request.user
    
    # Check if the user has already liked the post
    if post.likes.filter(user=user).exists():
        # User has liked it, so unlike it
        post.likes.filter(user=user).delete()
    else:
        # User hasn't liked it, so like it
        Like.objects.create(post=post, user=user)
        
    return redirect('post-detail', slug=post.slug)

def search(request):
    """Handles search queries for posts."""
    query = request.GET.get('q')
    posts = Post.objects.filter(status="published")
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(excerpt__icontains=query)
        ).distinct()
    
    context = {'posts': posts, 'query': query}
    context.update(get_base_context(request))
    return render(request, 'blog/search_results.html', context)