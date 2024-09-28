from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import Home, UserCreateAPIView, activate_account, ObtainTokenView, UserProfileAPIView, SearchEmail

app_name = 'authentication'

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', ObtainTokenView.as_view(), name='token_obtain_pair'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/<int:user_id>/<str:confirmation_code>/', activate_account, name='activate_account'),
    # Удалён маршрут для activate_logged_in_with_new_device
    path('profile/', UserProfileAPIView.as_view()),
    path('home/', Home.as_view(), name='home'),
    path('check_email/<str:email>/', SearchEmail.as_view()),
]
