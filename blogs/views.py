from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import( ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView)
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request, "blogs/home.html", context)

class BlogList(ListView):
    model=Blog
    template_name="blogs/home.html"
    context_object_name="posts"
    ordering=["-date_posted"]

class UserPostListView(ListView):
    model=Blog
    template_name="blogs/user_post.html"
    context_object_name="posts"
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get("username"))
        return Blog.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model=Blog

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    

class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model=Blog
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Blog
    success_url="/"

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request, 'blogs/about.html', {'title':'about'})
    