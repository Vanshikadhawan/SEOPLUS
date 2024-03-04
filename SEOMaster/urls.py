"""
URL configuration for SEOMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('ft',views.footer,name='footer'),
    path('login',views.login,name='login'),
    path('navbar',views.navbar,name='navbar'),
    path('register',views.register,name='register'),
    path('base',views.base,name='base'),
    path('allFAQs',views.allFAQs,name='faq'),
    path('allSearchEngines',views.allSearchEngines,name='searchengine'),
    path('allBlogs',views.allBlogs,name='blogs'),
    path('contact',views.contact,name='contact'),
    path('sidebar',views.sidebar,name='sidebar'),
    path('review',views.myreview,name='review'),
    path('ChangePassword',views.ChangePassword,name='changepassword'),
    path('HelpAndSupport',views.HelpAndSupport,name='helpandsupport'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('editProfile',views.editProfile,name='editprofile'),
    path('detailBlog/<int:id>',views.detailBlog, name="detailblog"),
    path('detailFAQ/<int:id>',views.detailFAQ, name="detailFAQ"),

    path('logout',views.logout,name='logout'),
    path('forgot',views.forgot,name='forgot'),







]

urlpatterns+=staticfiles_urlpatterns()
path('allBlogs',views.allBlogs),
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)