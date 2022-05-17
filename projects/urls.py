from django.urls import path
from projects.views import ProjectsListView, ProjectDetailView, ProjectEnrollmentView

urlpatterns = [
    path('', ProjectsListView.as_view()),
    path('/<int:project_id>', ProjectDetailView.as_view()),
    path('/enrollment', ProjectEnrollmentView.as_view()),
]
