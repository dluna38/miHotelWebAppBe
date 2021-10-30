from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rooms import views
from reservation.views.paymentViews import PaymentListView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('room/',include('rooms.urls')),
    path('guest/',include('guest.urls')),
    path('reservation/',include('reservation.urls')),
    path('payments/',PaymentListView.as_view())
]