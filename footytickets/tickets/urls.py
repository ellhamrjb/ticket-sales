from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet,TicketsViewSet

router = DefaultRouter()
router.register(r'events',EventViewSet)
router.register(r'tickets',TicketsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]