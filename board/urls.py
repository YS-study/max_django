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

    path('qna/<int:post_pk>/comments/', views.comments_create, name='comments_create'),
    path('qna/<int:post_pk>/comments/<int:comment_pk>/update/', views.comments_update, name='comments_update'),
    path('qna/<int:post_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]