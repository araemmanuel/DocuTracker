from django.urls import path
from .views import BeneficiaryListCreateView

urlpatterns = [
    path('create/', BeneficiaryListCreateView.as_view(), name='beneficiary-list-create'),
]
