from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('write/', views.board_write, name='board_write'),
    path('detail/<int:pk>/', views.board_detail, name='board_detail'),
    path('detail/<int:pk>/delete/', views.board_delete, name='board_delete'),
    path('detail/<int:pk>/update/', views.board_update, name='board_update'),
    path('detail/<int:pk>/comment/write', views.comment_write, name='cm-write')
]