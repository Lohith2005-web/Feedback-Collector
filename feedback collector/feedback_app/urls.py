from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_feedback, name='submit'),
    path('feedbacks/', views.show_feedbacks, name='feedbacks'),
]
