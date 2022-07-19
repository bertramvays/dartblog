from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_date(self):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic blog design'
        return context


class PostsByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_date(self):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    # данний метод нужен для увелечения количества просмотров. Здесь мы можем
    # что-то передать в контекст и выполнить какие-то действия с данными
    def get_context_date(self):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostsByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post'
    paginate_by = 1
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_date(self):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context