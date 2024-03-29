"""faceboop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from workplace_social import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('user/<username>/questions', views.questions),
    path('user/<username>/search', views.search),
    path('user/find-match', views.find_match),
    # path('user/<username>/', views.user_feed, name="user_feed"),
    # path('delete-post/<post_id>/', views.delete_post),
    # path('update-post/<post_id>/', views.update_post),
    path('users/', views.all_users, name="all_users"),
    path('admin/', admin.site.urls),
]
