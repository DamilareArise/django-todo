"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from todoManager.views import addTodo, home, editTodo, deleteTodo, handleComplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", TemplateView.as_view(template_name = "index.html"), name = 'home'),
    # path("get-todo-page/", TemplateView.as_view(template_name = "addTodopage.html"), name = 'get-todo-page'),
    path("add-todo/", addTodo, name = 'add-todo'),
    path ("", home, name = 'home'),
    path("edit-todo/<int:todo_id>/", editTodo, name = 'edit-todo'),
    path("delete-todo/<int:todo_id>/", deleteTodo, name = 'delete-todo'),
    path('handle-complete/<int:todo_id>/', handleComplete, name='handle-complete'),
    path("product/", include("productApp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("userApp/", include("userApp.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# model, (ORM -> object relational mapping) 
# view -> functionality of the app, 
# urls -> (uniform resource locator), 
'''
what makes up a url is 
1. path
2. view (functions)
3. name

'''
# forms -> , 
# template, -> template 

# def add():
#     print("Adding a new item")
    
# add()