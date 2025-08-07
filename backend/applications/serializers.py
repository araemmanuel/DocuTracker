from rest_framework import serializers
from .models import Claimant, Beneficiary, ApplicationForm, FamilyMember, Assessment
from django.contrib.auth import get_user_model

User = get_user_model()

class ClaimantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claimant
        fields = '__all__'


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = '__all__'


class ApplicationFormSerializer(serializers.ModelSerializer):
    claimant = ClaimantSerializer()
    beneficiary = BeneficiarySerializer()
    submitted_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = ApplicationForm
        fields = '__all__'

    def create(self, validated_data):
        claimant_data = validated_data.pop('claimant')
        beneficiary_data = validated_data.pop('beneficiary')
        claimant = Claimant.objects.create(**claimant_data)
        beneficiary = Beneficiary.objects.create(**beneficiary_data)
        application = ApplicationForm.objects.create(
            claimant=claimant,
            beneficiary=beneficiary,
            **validated_data
        )
        return application


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    assessed_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    application = serializers.PrimaryKeyRelatedField(queryset=ApplicationForm.objects.all())

    class Meta:
        model = Assessment
        fields = '__all__'
