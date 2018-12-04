from django.contrib.auth.decorators import login_required
from django.urls import path

from nsistanbul_job.views import AboutListCreateView, AboutRetrieveUpdateView, \
    CompanyListCreateView, CompanyRetrieveUpdateView,\
    CompanyAppListCreateView, CompanyAppRetrieveUpdateView,\
    ContributorListCreateView, ContributorRetrieveUpdateView, \
    JobListCreateView, JobRetrieveUpdateView,\
    URLGuide

# Describe Your URLs Here

urlpatterns = [
    # Guide
    path('', login_required(URLGuide.as_view()), name='url_guide'),
    # About
    path('about/', AboutListCreateView.as_view({'get': 'retrieve', 'post': 'create'}), name='about_list_create'),
    path('about/<pk>/', AboutRetrieveUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name='about_retrieve_update'),
    # Company
    path('company/', CompanyListCreateView.as_view({'get': 'list', 'post': 'create'}), name='company_list_create'),
    path('company/<pk>/', CompanyRetrieveUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name='company_retrieve_update'),
    # Company App
    path('companyapp/', CompanyAppListCreateView.as_view({'get': 'list', 'post': 'create'}), name='company_app_list_create'),
    path('companyapp/<pk>/', CompanyAppRetrieveUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name='company_app_retrieve_update'),
    # Contributor
    path('contributor/', ContributorListCreateView.as_view({'get': 'list', 'post': 'create'}), name='contributor_list_create'),
    path('contributor/<pk>/', ContributorRetrieveUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name='contributor_retrieve_update'),
    # Job
    path('job/', JobListCreateView.as_view({'get': 'list', 'post': 'create'}), name='job_list_create'),
    path('job/<pk>/', JobRetrieveUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name='job_retrieve_update')
]