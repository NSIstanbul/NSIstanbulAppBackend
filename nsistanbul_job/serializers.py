from rest_framework.serializers import ModelSerializer

from nsistanbul_job.models import Company, CompanyApp, Job

# Create Your Serializers Here.


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name',
            'email',
            'icon_url',
            'contact_url',
            'is_deleted',
            'created_at',
            'modified_at',
        ]


class CompanyAppSerializer(ModelSerializer):
    class Meta:
        model = CompanyApp
        fields = [
            'company',
            'name',
            'icon_url',
            'is_deleted',
            'created_at',
            'modified_at',
        ]


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'company',
            'position_title',
            'description',
            'city',
            'url',
            'is_active',
            'created_at',
            'modified_at',
        ]