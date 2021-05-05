from django.urls import path
from . import views

app_name = 'machines'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.index, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),

    # path('used/', views.used_index, name='used_index'),
    # path('used/<int:pk>', views.used_detail, name='used_detail'),
    # path('used/<int:pk>/delete/', views.used_delete, name='used_detail'),

    # path('new/', views.new_index, name='new_index'),
    # path('new/<int:pk>', views.new_detail, name='new_detail'),
    # path('new/<int:pk>/delete/', views.new_delete, name='new_delete'),    
]
