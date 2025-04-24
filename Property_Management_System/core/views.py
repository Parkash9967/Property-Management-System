from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum, Q

from .models import Contact, Unit, Lease
from .serializers import ContactSerializer, UnitSerializer, LeaseSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.select_related('unit', 'tenant', 'landlord')
    serializer_class = LeaseSerializer


# Custom Dashboard & Index Views
from rest_framework.views import APIView

class DashboardView(APIView):
    def get(self, request):
        total_units = Unit.objects.count()
        vacant_units = Unit.objects.filter(status='vacant').count()
        occupied_units = Unit.objects.filter(status='occupied').count()

        landlords = Contact.objects.filter(contact_type='landlord').annotate(unit_count=Count('unit'))
        landlord_data = [{ "name": l.name, "units": l.unit_count } for l in landlords]

        total_rent = Lease.objects.aggregate(total=Sum('rent_amount'))['total'] or 0

        lease = Lease.objects.select_related('unit', 'tenant', 'landlord').first()

        return Response({
            "total_units": total_units,
            "vacant_units": vacant_units,
            "occupied_units": occupied_units,
            "landlords": landlord_data,
            "total_rent_income": total_rent,
            "test_lease": LeaseSerializer(lease).data if lease else None,
        })


class IndexView(APIView):
    def get(self, request):
        lease = Lease.objects.select_related('unit', 'tenant', 'landlord').first()
        if not lease:
            return Response({"message": "No test lease found"})
        return Response(LeaseSerializer(lease).data)
