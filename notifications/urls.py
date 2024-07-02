from django.urls import path
#from .views import LoginAPIView, SendEmailAPIView
from notifications.views import NotificationAPIView

urlpatterns = [
#    path('auth/login/', LoginAPIView.as_view(), name='login'),
path('send/', NotificationAPIView.as_view(), name='send_email'),
]