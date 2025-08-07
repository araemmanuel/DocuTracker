from django.db import models

class Workflow(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class WorkflowStep(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100,default="Sup")
    order = models.PositiveIntegerField(help_text="Step order in the workflow")
    required_role = models.CharField(max_length=100, help_text="e.g., Social Worker, Department Head")

    def __str__(self):
        return f"{self.workflow.name} - Step {self.order}: {self.name}"
    
    class Meta:
        ordering = ['workflow', 'order']
        unique_together = ('workflow', 'order')
# tester