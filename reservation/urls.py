from django.urls import path
from .views.reservationViews import ReservationCreateView,ReservationListView,ReservationDetailView,ReservationUpdateView,ReservationDeleteView
from .views.paymentViews import *
app_name='reservation'

#reservation/
urlpatterns = [
    path('', ReservationListView.as_view(),name='reservation-list'),
    path('create/',ReservationCreateView.as_view(),name='reservation-create'),
    path('<int:pk>/', ReservationDetailView.as_view(),name='reservation-detail'),
    path('<int:pk>/update',ReservationUpdateView.as_view(),name='reservation-update'),
    path('<int:pk>/delete',ReservationDeleteView.as_view(),name='reservation-delete'),
    path('<int:pk>/payment',PaymentDetailView.as_view()),
    path('<int:pk>/payment/create',PaymentCreateView.as_view()),
    path('<int:pk>/payment/update',PaymentUpdateView.as_view()),
    path('<int:pk>/payment/delete',PaymentDeleteView.as_view()),
]