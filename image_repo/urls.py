"""image_repo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from repo_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='home'),
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('success/', views.success, name='success'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('profile/<int:user_id>/', views.Profile.as_view(), name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.Upload.as_view(), name='upload'),    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


