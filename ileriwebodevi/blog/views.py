from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
import django_filters

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Başlık')  # Başlık içeriğine göre arama
    ordering = django_filters.OrderingFilter(
        choices=[
            ('date_created', 'En Eski'),
            ('-date_created', 'En Yeni'),
        ],
        label='Sırala'  # Açılır menü etiketi
    )

    class Meta:
        model = PostModel
        fields = ['title']



# Ana sayfa (index) view fonksiyonu
@login_required
def index(request):
    post_filter = PostFilter(request.GET, queryset=PostModel.objects.all())
    posts = post_filter.qs  # Filtrelenmiş sonuçları alıyoruz

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()

    context = {
        'posts': posts,
        'form': form,
        'filter': post_filter  # Filtreyi template'e gönderiyoruz
    }

    return render(request, 'blog/index.html', context)


# Post detay sayfası
@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()

    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'blog/post_detail.html', context)


# Post düzenleme sayfası
@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)


# Post silme sayfası
@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)
