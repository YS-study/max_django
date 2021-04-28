from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Post, Question, Answer
from .forms import PostForm, QuestionForm, AnswerForm
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required


# 메인
def notice(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts
    }
    return render(request, 'notice/index.html', context)

# C
@login_required
@require_http_methods(['GET', 'POST'])
def notice_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('board:notice_detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'notice/create_update.html', context)

# R
def notice_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'notice/detail.html', context)

# U
@login_required
@require_http_methods(['GET', 'POST'])
def notice_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('board:notice_detail', pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('board:notice')
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'notice/create_update.html', context)

# D
@require_POST
def notice_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        if request.user == post.user:
            post.delete()
            return redirect('board:notice')
    return redirect('board:detail', pk)




def qna(request):
    pass
# C
def qna_create(request):
    pass
# R
def qna_detail(request, pk):
    pass
# U 
def qna_update(request, pk):
    pass
# D
def qna_delete(request, pk):
    pass




# R
def comments_create(request, post_pk):
    pass
# U 
def comments_update(request, post_pk, comment_pk):
    pass
# D
def comments_delete(request, post_pk, comment_pk):
    pass
