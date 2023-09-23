from django.urls import path
from accounts.views import CreateUserAPI, UpdateUserAPI, LoginUserAPI
from knox.views import LogoutAllView, LogoutView
from hospital.views import TodoList, TodoDetails

urlpatterns = [
    path('create-user/', CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', UpdateUserAPI.as_view()),
    path('login/',LoginUserAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),

    path('todo/', TodoList.as_view()),
    path('todo-details/<int:pk>/',TodoDetails.as_view()),
]
