from django.urls import path

from webapp.views.base import IndexView
from webapp.views.tasks import TaskDetail, TaskUpdateView, TaskDeleteView, TaskAddView

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path("task/", IndexView.as_view()),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('task/add/', TaskAddView.as_view(), name='task_add'),

]
