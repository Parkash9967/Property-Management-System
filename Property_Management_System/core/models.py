from django.db import models

class Contact(models.Model):
    CONTACT_TYPES = (
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    )

    name = models.CharField(max_length=100)
    contact_type = models.CharField(max_length=10, choices=CONTACT_TYPES)
    contact_info = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.contact_type})"


class Unit(models.Model):
    UNIT_STATUS = (
        ('vacant', 'Vacant'),
        ('occupied', 'Occupied'),
    )

    unit_number = models.CharField(max_length=10)
    unit_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=UNIT_STATUS, default='vacant')
    owner = models.ForeignKey(Contact, on_delete=models.CASCADE, limit_choices_to={'contact_type': 'landlord'})

    def __str__(self):
        return f"{self.unit_number} - {self.status}"


class Lease(models.Model):
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tenant_leases', limit_choices_to={'contact_type': 'tenant'})
    landlord = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='landlord_leases', limit_choices_to={'contact_type': 'landlord'})
    start_date = models.DateField()
    duration_months = models.PositiveIntegerField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(max_length=20)  # e.g. Monthly, Quarterly

    def __str__(self):
        return f"Lease of {self.unit.unit_number} by {self.tenant.name}"
