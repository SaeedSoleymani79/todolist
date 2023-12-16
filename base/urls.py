from django.urls import path
from . import views
from .views import  TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, upload
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('html/', views.html, name='html'),
    path('upload/', views.upload, name='upload'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='task'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]

# We didn't create a logout functionality in our views because we can just simply import LogoutView here and just declare its path.
# The path for logout view would be /logout/ which lead the user to login page.