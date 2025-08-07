from django.db import models
from django.conf import settings
from approvals.models import ApplicationForm

class ApplicationHistory(models.Model):
    EVENT_TYPES = [
        ('status_change', 'Status Change'),
        ('comment', 'Comment'),
        ('print', 'Print'),
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In Transit'),
        ('received', 'Received'),
    ]

    application = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name='history')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    old_status = models.CharField(max_length=50, blank=True, null=True)
    new_status = models.CharField(max_length=50, blank=True, null=True)
    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='change_logs'
    )
    notes = models.TextField(blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application} - {self.event_type} @ {self.changed_at}"
