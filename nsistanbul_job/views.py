from django.views.generic import TemplateView
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from nsistanbul_job.models import About, Company, CompanyApp, Contributor, Job
from nsistanbul_job.serializers import AboutSerializer, CompanySerializer, CompanyAppSerializer, ContributorSerializer, JobSerializer


# Create your views here.

# ---------------------- API URL Guide ----------------------


class URLGuide(TemplateView):
    template_name = 'guide.html'


# ------------------------- Company -------------------------


class CompanyListCreateView(ModelViewSet):
    model = Company
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]


class CompanyRetrieveUpdateView(ModelViewSet):
    model = Company
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Company.objects.filter(is_deleted=False, id=pk)
        return queryset


# ------------------------- Company App -------------------------


class CompanyAppListCreateView(ModelViewSet):
    model = CompanyApp
    serializer_class = CompanyAppSerializer
    queryset = CompanyApp.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]


class CompanyAppRetrieveUpdateView(ModelViewSet):
    model = CompanyApp
    serializer_class = CompanyAppSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = CompanyApp.objects.filter(is_deleted=False, id=pk)
        return queryset

# ------------------------- Job -------------------------


class JobListCreateView(ModelViewSet):
    model = Job
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [IsAuthenticated]


class JobRetrieveUpdateView(ModelViewSet):
    model = Job
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Job.objects.filter(is_deleted=False, id=pk)
        return queryset


# ------------------------- About -------------------------


class AboutListCreateView(ModelViewSet):
    model = About
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = About.objects.first()
        return queryset


class AboutRetrieveUpdateView(ModelViewSet):
    model = About
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = About.objects.filter(is_deleted=False, id=pk)
        return queryset


# ------------------------- Contributor -------------------------


class ContributorListCreateView(ModelViewSet):
    model = Contributor
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [IsAuthenticated]


class ContributorRetrieveUpdateView(ModelViewSet):
    model = Contributor
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Contributor.objects.filter(is_deleted=False, id=pk)
        return queryset
