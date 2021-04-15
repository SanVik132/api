"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from web.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',register.as_view(),name = 'register'),
    path('accounts/register/confirm/', ConfirmuserView.as_view(), name='userconfirm'),
    path('forgotpassword/',Forgotpwdview.as_view(),name = 'forgotpassword'),
    path('forgotpassword/confirm/',ConfirmpwdotpView.as_view(),name = 'confirmforgotpassword'),
    path('newpassword/',NewpasswordView.as_view(),name = 'newpassword'),
    
    path('student/',StudentDetailsView.as_view({
        'get':'list',
        'post':'create',
        })),
    path('student/<int:pk>/',StudentDetailsView.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
        })),

    path('teacher/',TeacherDetailsView.as_view({
        'get':'list',
        'post':'create',
        })),
    path('teacher/<int:pk>/',TeacherDetailsView.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
        })),




        
]
