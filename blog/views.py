from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin
                                        )
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

posts = Post.objects.all()


def home(request):
    return render(request, 'blog/home.html', {'posts': posts})


class PostListView(ListView):
    model = Post   # This view passes object_list to my template.
    # tempname <app>/<model>_<viewtype>.html


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {})


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
