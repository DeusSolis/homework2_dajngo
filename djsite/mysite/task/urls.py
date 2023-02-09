from django.urls import path
from task.views import task_list_view, task_details_view

urlpatterns = [
    path("", task_list_view, name="task_list"),
    path("<int:id>/", task_details_view, name="task_detail")

]
