from rest_framework import serializers
from .models import Contact, Unit, Lease

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    owner = ContactSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.filter(contact_type='landlord'),
        source='owner',
        write_only=True
    )

    class Meta:
        model = Unit
        fields = ['id', 'unit_number', 'unit_type', 'location', 'value', 'status', 'owner', 'owner_id']


class LeaseSerializer(serializers.ModelSerializer):
    tenant = ContactSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.filter(contact_type='tenant'),
        source='tenant',
        write_only=True
    )

    landlord = ContactSerializer(read_only=True)
    landlord_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.filter(contact_type='landlord'),
        source='landlord',
        write_only=True
    )

    unit = UnitSerializer(read_only=True)
    unit_id = serializers.PrimaryKeyRelatedField(
        queryset=Unit.objects.all(),
        source='unit',
        write_only=True
    )

    class Meta:
        model = Lease
        fields = ['id', 'unit', 'unit_id', 'tenant', 'tenant_id', 'landlord', 'landlord_id',
                  'start_date', 'duration_months', 'rent_amount', 'payment_frequency']
