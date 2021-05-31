"""ya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include

from django.urls import path
from first.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_start_page, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup_view, name="signup"),
    path('profile/', view_profile, name="view_profile"),
    path('upload_image/', upload_image, name="upload_image"),
    path('change_avatar/', change_avatar, name="change_avatar"),
    path('<int:image_id>', like, name="like"),
    path('edit_page/', view_edit_page, name="edit_page"),
    path('become_user/', become_user, name="become_user"),
    path('become_photographer/', become_photographer, name="become_photographer"),
    path('users/<int:user_need>', view_user_profile, name="view_user_profile"),
    path('order/', order, name="order"),
    path('messages/', show_messages_page, name="messages"),
    path('list/', show_list_page, name="list"),
    path('notifications/', show_notifications_page, name="notifications"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
