"""
This module defines URL patterns for the todo app.
"""

from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "todo"


# Urls for to-done app
urlpatterns = [
    path('', views.index, name='index'),
    path('todo', views.index, name='todo'),
    path('todo/<int:list_id>', views.index, name='todo_list_id'),
    path('todo/new-from-template', views.todo_from_template, name='todo_from_template'),
    path('delete-todo', views.delete_todo, name='delete_todo'),
    path('templates', views.template, name='template'),
    path('templates/<int:template_id>', views.template, name='template'),
    path('templates/new-from-todo', views.template_from_todo, name='template_from_todo'),
    path('updateListItem', views.updateListItem, name='updateListItem'),
    path('removeListItem', views.removeListItem, name='removeListItem'),
    path('createNewTodoList', views.createNewTodoList, name='createNewTodoList'),
    path('getListItemByName', views.getListItemByName, name='getListItemByName'),
    path('getListItemById', views.getListItemById, name='getListItemById'),
    path('markListItem', views.markListItem, name='markListItem'),
    path('addNewListItem', views.addNewListItem, name='addNewListItem'),
    path('updateListItem/<int:item_id>', views.updateListItem, name='updateListItem'),
    path('send_push', views.send_push, name='send_push'),
    path('checkForNotifications', views.checkForNotifications, name='checkForNotifications'),
    path('webpush/', include('webpush.urls')),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path(
        'sw.js',
        TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'),
        name="sw.js"
    )
]
