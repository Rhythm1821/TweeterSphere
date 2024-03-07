from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile_list/',views.profile_list,name='profile_list'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('update-user/',views.update_user,name='update-user'),
    path('tweet-like/<int:pk>',views.tweet_like,name='tweet-like'),
    path('tweet-show/<int:pk>',views.tweet_show,name='tweet-show'),
    path('unfollow/<int:pk>',views.unfollow,name='unfollow'),
]