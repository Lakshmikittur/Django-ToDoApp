from django.urls import path
from .views import (
    home_view,
    create_task_view,
    update_task_view,
    task_detail_view, 
    delete_task_view
)

app_name = "tasks"
urlpatterns = [
    path('', home_view, name="homeview"),
    path('createtask/', create_task_view, name="createtask"),
    path('<int:id>/', task_detail_view, name="taskdetail"),
    path('updatetask/<int:id>', update_task_view, name="updatetask"),
    path('deletetask/<int:id>', delete_task_view, name="deletetask")
]