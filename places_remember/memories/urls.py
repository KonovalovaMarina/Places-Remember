from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('social_auth/', include('social_django.urls', namespace='social')),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('add_memory/', views.add_memory, name='add_memory'),
    path('delete_memory/<str:memory_id>', views.delete_memory, name='delete_memory'),
]
