"""drf_filtering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from core.views import (CategoryTopLevel, CategoryView, CategoryDetail, ExternalCategoryCreateView,
                        ExternalCategoryListView, AssociationCreateView, AssociationListView)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Category
    url(r'^categories-top-level/$', CategoryTopLevel.as_view(), name='category-top-level'),
    url(r'^categories/$', CategoryView.as_view(), name='categories'),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category'),
    # External category
    url(r'^external-category/$', ExternalCategoryCreateView.as_view(), name='external-category'),
    url(r'^external-categories/$', ExternalCategoryListView.as_view(), name='external-categories'),
    # Association
    url(r'^association/$', AssociationCreateView.as_view(), name='association'),
    url(r'^associations/$', AssociationListView.as_view(), name='associations'),
]
