from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView,)
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, "blogs/home.html", context=context)

def about(request):
    return render(request, "blogs/about.html", {'title':'About'})

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blogs/home.html'
    ordering = ['-date_posted']

class userPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blogs/user_posts.html'
    paginate_by=5

    def get_queryset(self):
        user = get_object_or_404(User, email=self.kwargs.get("email"))
        return Post.objects.filter(author=user).order_by("-date_posted")



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(DeleteView):
    model = Post
    success_url='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

    
