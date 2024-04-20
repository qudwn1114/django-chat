from django.urls.conf import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home',),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='chat:home'), name='logout'),
    path('chat/<str:room_name>/', views.ChatRoomView.as_view(), name='room'),
]