from decimal import Decimal
from django.db import models
from django.conf import settings

GENDER_CHOICES = [
    (None, 'Unknown'),
    ('male', 'Male'),
    ('female', 'Female'),
]

CIVIL_STATUS_CHOICES = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('widowed', 'Widowed'),
    ('separated', 'Separated'),
    ('divorced', 'Divorced'),
    ('annulled', 'Annulled'),
    ('cohabiting', 'Cohabiting / Live-in'),
    ('unknown', 'Prefer not to say'),
]

EDUCATIONAL_ATTAINMENT_CHOICES = [
    ('none', 'No Formal Education'),
    ('elem_incomplete', 'Elementary Level (Incomplete)'),
    ('elem_graduate', 'Elementary Graduate'),
    ('hs_incomplete', 'High School Level (Incomplete)'),
    ('hs_graduate', 'High School Graduate'),
    ('shs_incomplete', 'Senior High School (Incomplete)'),
    ('shs_graduate', 'Senior High School Graduate'),
    ('vocational', 'Vocational Graduate'),
    ('college_incomplete', 'College Level (Incomplete)'),
    ('college_graduate', 'College Graduate'),
    ('postgrad', 'Postgraduate / Master’s Degree'),
    ('doctorate', 'Doctoral Degree / PhD'),
]

class Claimant(models.Model):
    RELATIONSHIP_CHOICES = [
        ('self', 'Self'),
        ('spouse', 'Spouse'),
        ('child', 'Child'),
        ('parent', 'Parent'),
        ('sibling', 'Sibling'),
        ('grandparent', 'Grandparent'),
        ('grandchild', 'Grandchild'),
    ]

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,null=True, blank=True)
    extension_name = models.CharField(max_length=100,null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True)
    contact_number = models.CharField(max_length=13,null=True, blank=True)
    educational_attainment = models.CharField(max_length=30, choices=EDUCATIONAL_ATTAINMENT_CHOICES, null=True, blank=True)
    civil_status = models.CharField(max_length=15, choices=CIVIL_STATUS_CHOICES, null=True, blank=True)
    occupation = models.TextField(default='None', blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), blank=True)
    relationship_to_beneficiary = models.CharField(max_length=12, choices=RELATIONSHIP_CHOICES, default='self')
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Beneficiary(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,null=True, blank=True)
    extension_name = models.CharField(max_length=100,null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True)
    contact_number = models.CharField(max_length=13,null=True, blank=True)
    educational_attainment = models.CharField(max_length=30, choices=EDUCATIONAL_ATTAINMENT_CHOICES, null=True, blank=True)
    civil_status = models.CharField(max_length=15, choices=CIVIL_STATUS_CHOICES, null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ApplicationForm(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('in_transit', 'In Transit'),
        ('awaiting_delivery', 'Awaiting Delivery'),
        ('received', 'Received'),
        ('printed', 'Printed'),
    ]

    claimant = models.ForeignKey(Claimant, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    reference_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Application #{self.reference_number} - {self.status}"

class FamilyMember(models.Model):
    claimant = models.ForeignKey(Claimant, on_delete=models.CASCADE, related_name='family_members')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True)
    educational_attainment = models.CharField(max_length=30, choices=EDUCATIONAL_ATTAINMENT_CHOICES, null=True, blank=True)
    government_employee = models.BooleanField(default=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2,default=Decimal('0.00'))

    def __str__(self):
        return f"{self.name} ({self.age})"

class Assessment(models.Model):
    application = models.OneToOneField(ApplicationForm, on_delete=models.CASCADE)
    issue_description = models.TextField(default='WAS NOT DETERMINED')
    worker_assessment = models.TextField(default='WAS NOT ASSESSED')
    risk_level = models.CharField(max_length=50,null=True)  # e.g., 'Low', 'Moderate', 'High'
    assessed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    assessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assessment for Application #{self.application.reference_number}"
