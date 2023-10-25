from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsList(ListView):
    model = Post
    ordering = '-in_time'
    template_name = 'news/posts.html'
    context_object_name = 'posts_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostsSearch(ListView):
    model = Post
    ordering = '-in_time'
    template_name = 'news/search.html'
    context_object_name = 'search_result'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


#   PostNewsCreate, PostNewsUpdate, PostNewsDelete,

class PostNewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', 'news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'N'
        return super().form_valid(form)


class PostNewsUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.add_post', 'news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def get_queryset(self):
        return super().get_queryset().filter(type='N')


class PostNewsDelete(DeleteView):
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('posts_list_name')

    def get_queryset(self):
        return super().get_queryset().filter(type='N')


#    PostArticleCreate, PostArticleUpdate, PostArticleDelete

class PostArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', 'news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'A'
        return super().form_valid(form)


class PostArticleUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.add_post', 'news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def get_queryset(self):
        return super().get_queryset().filter(type='A')


class PostArticleDelete(DeleteView):
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('posts_list_name')

    def get_queryset(self):
        return super().get_queryset().filter(type='A')
