"""table_wisdom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from signup import views as sign_up_views
from dashboard import views as dashboard_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'templates/login.html'},  name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^dashboard/$', dashboard_views.dashboard, name='home' ),
    url(r'^signup/$', sign_up_views.basic_info, name='signup'),
#    url(r'^user_registration/', views.user_registration, name='user_registration' ),

]
