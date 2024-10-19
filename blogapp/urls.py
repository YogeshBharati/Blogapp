from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('post<int:post_id>/',views.single_post,name='single_post')
    ]
