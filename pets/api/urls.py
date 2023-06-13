from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BreedViewSet, AnimalClassViewSet

router_v1 = DefaultRouter()
router_v1.register(r'breed', BreedViewSet)
router_v1.register(r'animal-classes', AnimalClassViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
