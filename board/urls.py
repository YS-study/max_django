from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('notice/create/', views.notice_create, name='notice_create'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('notice/<int:pk>/update/', views.notice_update, name='notice_update'),
    path('notice/<int:pk>/delete/', views.notice_delete, name='notice_delete'),

    path('qna/', views.qna, name='qna'),
    path('qna/create/', views.qna_create, name='qna_create'),
    path('qna/<int:pk>/', views.qna_detail, name='qna_detail'),
    path('qna/<int:pk>/update/', views.qna_update, name='qna_update'),
    path('qna/<int:pk>/delete/', views.qna_delete, name='qna_delete'),

    path('qna/<int:question_pk>/answers/', views.answers_create, name='answers_create'),
    path('qna/<int:question_pk>/answers/<int:answer_pk>/update/', views.answers_update, name='answers_update'),
    path('qna/<int:question_pk>/answers/<int:answer_pk>/delete/', views.answers_delete, name='answers_delete'),
]