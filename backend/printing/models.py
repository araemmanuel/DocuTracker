from django.db import models
from django.conf import settings
from approvals.models import ApplicationForm

class PrintLog(models.Model):
    application = models.ForeignKey(
        ApplicationForm,
        on_delete=models.CASCADE,
        related_name='print_logs'
    )
    printed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='printed_applications'
    )
    printed_at = models.DateTimeField(auto_now_add=True)
    print_details = models.TextField(blank=True, help_text="Printer settings, number of copies, etc.")

    def __str__(self):
        return f"Printed {self.application} by {self.printed_by} on {self.printed_at}"
