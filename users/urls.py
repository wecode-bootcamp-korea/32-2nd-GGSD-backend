from django.urls import path

from users.views import KakaoLoginView, UserDetailView


urlpatterns = [
    path('/detail', UserDetailView.as_view()),
    path('/login', KakaoLoginView.as_view())
]
