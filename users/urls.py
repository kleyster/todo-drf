from django.urls import path
from .views import RegistrationView,UserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = (
    path('registration/',RegistrationView.as_view()),
    path('me/',UserView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
)