from django.urls import path
from . import views

urlpatterns = [ path('task/', views.TaskList.as_view()),
                path('detail/<int:pk>', views.TaskDetailView.as_view(), name='detail'),

]