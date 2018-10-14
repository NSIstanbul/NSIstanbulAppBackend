from rest_framework.serializers import ModelSerializer, SerializerMethodField

from nsistanbul_job.models import About, Company, CompanyApp, Contributor, Job

# Create Your Serializers Here.


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'name',
            'email',
            'icon_url',
            'contact_url',
            'is_deleted',
            'created_at',
            'modified_at'
        )


class CompanyAppSerializer(ModelSerializer):

    class Meta:
        model = CompanyApp
        fields = (
            'company',
            'name',
            'icon_url',
            'is_deleted',
            'created_at',
            'modified_at'
        )


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = (
            'company',
            'position_title',
            'description',
            'city',
            'url',
            'is_active',
            'created_at',
            'modified_at'
        )


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = (
            'id',
            'name',
            'avatar_url',
            'external_url',
            'is_active',
            'is_deleted',
            'created_at',
            'modified_at'
        )


class AboutSerializer(ModelSerializer):
    contributor = ContributorSerializer(read_only=True, many=True)

    class Meta:
        model = About
        fields = (
            'description',
            'contributor',
            #'contributors',
            'is_active',
            'is_deleted',
            'created_at',
            'modified_at'
        )
