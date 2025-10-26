from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import DestinationViewSet

router = DefaultRouter()
router.register('api/destinations', DestinationViewSet)

urlpatterns= [
    path('', views.home, name='home'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('destination/add/', views.add_destination, name='add_destination'),
    path('destination/<int:pk>/edit/', views.edit_destination, name='edit_destination'),
    path('destination/<int:pk>/delete/', views.delete_destination, name='delete_destination'),

]
urlpatterns += router.urls