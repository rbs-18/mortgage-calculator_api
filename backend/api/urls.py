from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OfferViewSet

router = DefaultRouter()
router.register('offer', OfferViewSet, basename='offer')

urlpatterns = [
    path('v1/', include(router.urls)),
]
