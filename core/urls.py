"""core URL Configuration

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
from django.urls import include, path
from books import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.books, name="books"),
    path("add/", views.BookFormView.as_view(), name="add_books"),
    path("import/", views.import_books, name="import_books"),
    path("docs/", views.ApiDocsView.as_view(), name="api_docs"),
    path("api/", include("api.urls")),
]
