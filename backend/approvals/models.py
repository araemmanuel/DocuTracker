from django.db import models
from django.conf import settings
from workflows.models import WorkflowStep
from applications.models import ApplicationForm

class Approval(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    application_form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name='approvals')
    step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE)
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comments = models.TextField(blank=True)
    actioned_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('application_form', 'step')
        ordering = ['application_form', 'step']

    def __str__(self):
        return f"{self.application_form} - {self.step.name} - {self.status}"
