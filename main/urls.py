from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("tasks/", views.TaskListView.as_view(), name="task_list"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("tasks/<int:pk>/toggle_status/", views.toggle_task_status, name="task_toggle_status"),
]
