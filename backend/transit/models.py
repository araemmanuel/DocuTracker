from django.db import models
from django.conf import settings
from applications.models import ApplicationForm
from workflows.models import WorkflowStep
from locations.models import Location

class TransitRecord(models.Model):
    STATUS_CHOICES = [
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In Transit'),
        ('received', 'Received'),
    ]

    application_form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name='transits')
    from_step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE, related_name='transits_sent')
    to_step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE, related_name='transits_received')
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='transits_from')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='transits_to')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='dispatched')
    expected_arrival = models.DateTimeField(null=True, blank=True)
    actual_arrival = models.DateTimeField(null=True, blank=True)
    handled_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Transit for {self.application_form} from {self.from_location} to {self.to_location}"
