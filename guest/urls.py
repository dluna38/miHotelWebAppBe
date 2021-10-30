from django.urls import path
from .views.guestViews import GuestCreateView,GuestListView,GuestDetailView,GuestUpdateView,GuestDeleteView

app_name='guest'

urlpatterns = [
    path('', GuestListView.as_view(),name='guest-list'),
    path('create/',GuestCreateView.as_view(),name='guest-create'),
    path('<int:pk>/', GuestDetailView.as_view(),name='guest-detail'),
    path('<int:pk>/update',GuestUpdateView.as_view(),name='guest-update'),
    path('<int:pk>/delete',GuestDeleteView.as_view(),name='guest-delete'),
]