from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import models
from .views import PostUpdateView, PostDeleteView



urlpatterns = [
    path('', views.HomeDetail.as_view(), name='index'),
    path('home/', views.PostList.as_view(), name='home'),
    path('create/', views.create_post, name = 'create'),
    path('search/', views.search, name='search'),
    #path('post/<str:id>', views.PostDetail, name='details'),
    #path('profile/', views.userProfile.as_view(), name='profile'),
    path('uploads/', views.PostList.as_view(), name = 'uploads'),
    path('<slug:slug>/', views.PostDetail.as_view(), name= 'details'),
    path('post/<slug:slug>/edit', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),

    #path('post/<int:pk>', views.PostDetail.as_view(), name='post_details'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root = settings.MEDIA_ROOT)


