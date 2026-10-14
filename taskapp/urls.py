from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    # path("complete/<int:pk>/", views.complete_task, name="complete_task"),
    path("complete/<int:pk>/", views.TaskCompleteView.as_view(), name="complete_task"),
    # path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete_task"),
]
