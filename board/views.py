from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Post, Question, Answer
from .forms import PostForm, QuestionForm, AnswerForm
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# 메인
def notice(request):
    posts = Post.objects.order_by('-pk')
    
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    max_index = posts.paginator.num_pages
    current_index = posts.number
    th = current_index // 6
    if max_index >= 5*th+6:
        current_page_range = range(5*th+1, 5*th+6)
    else:
        current_page_range = range(5*th+1, max_index+1)

    context = {
        'posts': posts,
        'current_page_range': current_page_range,
        'menu': '공지사항'
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
        'menu': '공지사항',
    }
    return render(request, 'notice/create_update.html', context)

# R
def notice_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'menu': '공지사항',
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
        'menu': '공지사항',
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
    questions = Question.objects.order_by('-pk')

    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    questions = paginator.get_page(page_number)

    max_index = questions.paginator.num_pages
    current_index = questions.number
    th = current_index // 6
    if max_index >= 5*th+6:
        current_page_range = range(5*th+1, 5*th+6)
    else:
        current_page_range = range(5*th+1, max_index+1)

    context = {
        'questions': questions,
        'current_page_range': current_page_range,
        'menu': '1:1 문의',
    }
    return render(request, 'qna/index.html', context)

# C
@require_http_methods(['GET', 'POST'])
def qna_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('board:qna_detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
        'menu': '1:1 문의'
    }
    return render(request, 'qna/create_update.html', context)


# R
def qna_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answer_form = AnswerForm()
    answers = question.answer_set.all()
    context = {
        'question': question,
        'answer_form': answer_form,
        'answers': answers,
        'menu': '1:1 문의',
    }
    return render(request, 'qna/detail.html', context)

# U 
@require_http_methods(['GET', 'POST'])
def qna_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect('board:qna_detail', question.pk)
    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form,
        'menu': '1:1 문의',
    }
    return render(request, 'qna/create_update.html', context)


# D
@require_POST
def qna_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('board:qna')




# R
@require_POST
@login_required
def answers_create(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    answer_form = AnswerForm(request.POST)
    if answer_form.is_valid():
        answer = answer_form.save(commit=False)
        answer.question = question
        answer.user = request.user
        answer.save()
    return redirect('board:qna_detail', question_pk)


# U 
def answers_update(request, question_pk, answer_pk):
    pass

# D
@require_POST
@login_required
def answers_delete(request, question_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    answer.delete()
    return redirect('board:qna_detail', question_pk)
