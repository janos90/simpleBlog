from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post, Category


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'update_category.html'
    # form_class = CategoryForm

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('home')


class CategoryDetailView(ListView):
    model = Category
    template_name = 'category_detail.html'
