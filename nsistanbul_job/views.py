from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet

from nsistanbul_job.models import Company, CompanyApp, Job
from nsistanbul_job.serializers import CompanySerializer, CompanyAppSerializer, JobSerializer


# Create your views here.

# ---------------------- API URL Guide ----------------------


class URLGuide(TemplateView):
    template_name = 'guide.html'


# ------------------------- Company -------------------------


class CompanyListCreateView(ModelViewSet):
    model = Company
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(is_deleted=False)


class CompanyRetrieveUpdateView(ModelViewSet):
    model = Company
    serializer_class = CompanySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Company.objects.filter(is_deleted=False, id=pk)
        return queryset


# ------------------------- Company App -------------------------


class CompanyAppListCreateView(ModelViewSet):
    model = CompanyApp
    serializer_class = CompanyAppSerializer
    queryset = CompanyApp.objects.filter(is_deleted=False)


class CompanyAppRetrieveUpdateView(ModelViewSet):
    model = CompanyApp
    serializer_class = CompanyAppSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = CompanyApp.objects.filter(is_deleted=False, id=pk)
        return queryset

# ------------------------- Job -------------------------


class JobListCreateView(ModelViewSet):
    model = Job
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True, is_deleted=False)


class JobRetrieveUpdateView(ModelViewSet):
    model = Job
    serializer_class = JobSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Job.objects.filter(is_deleted=False, id=pk)
        return queryset
