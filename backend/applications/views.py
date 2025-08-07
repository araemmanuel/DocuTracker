from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    ApplicationForm,
    Claimant,
    Beneficiary,
    FamilyMember,
    Assessment
)
from .serializers import (
    ApplicationFormSerializer,
    ClaimantSerializer,
    BeneficiarySerializer,
    FamilyMemberSerializer,
    AssessmentSerializer
)
from rest_framework.permissions import IsAuthenticated


# ApplicationForm Views

class ApplicationFormListCreateView(generics.ListCreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)


class ApplicationFormDetailView(generics.RetrieveAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


# Claimant Views

class ClaimantListCreateView(generics.ListCreateAPIView):
    queryset = Claimant.objects.all()
    serializer_class = ClaimantSerializer
    permission_classes = [IsAuthenticated]


# Beneficiary Views

class BeneficiaryListCreateView(generics.ListCreateAPIView):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    permission_classes = [IsAuthenticated]


# FamilyMember Views

class FamilyMemberListCreateView(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
    permission_classes = [IsAuthenticated]


# Assessment Views

class AssessmentListCreateView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(assessed_by=self.request.user)
