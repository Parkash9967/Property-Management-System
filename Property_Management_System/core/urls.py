from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, UnitViewSet, LeaseViewSet, DashboardView, IndexView

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'units', UnitViewSet)
router.register(r'leases', LeaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('summary/', IndexView.as_view(), name='summary'),
]
