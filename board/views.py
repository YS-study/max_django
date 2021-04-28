from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Post, Comment
from .forms import PostForm, CommentForm

# 메인
def notice(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts
    }
    return render(request, 'notice/index.html', context)

# C
def notice_create(request):
    pass

# R
def notice_detail(request, pk):
    pass

# U
def notice_update(request, pk):
    pass

# D
def notice_delete(request, pk):
    pass




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
