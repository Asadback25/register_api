from django.urls import path
from .views import CustomUserList, CustomUserRegister , CustomUserDelete
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
urlpatterns = [
    path('list/', CustomUserList.as_view()),
    path('register/', CustomUserRegister.as_view()),
    path('delete/<uuid:id>/', CustomUserDelete.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]