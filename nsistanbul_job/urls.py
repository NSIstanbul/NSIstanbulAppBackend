from django.urls import path

from nsistanbul_job.views import CompanyListCreateView, CompanyRetrieveUpdateView,\
    CompanyAppListCreateView, CompanyAppRetrieveUpdateView,\
    JobListCreateView, JobRetrieveUpdateView,\
    URLGuide

# Describe Your URLs Here

urlpatterns = [
    path('', URLGuide.as_view(), name='url_guide'),
    path('company/', CompanyListCreateView.as_view({'get':'list','post':'create'}), name='company_list_create'),
    path('company/<pk>/', CompanyRetrieveUpdateView.as_view({'get':'retrieve','put':'update'}), name='company_retrieve_update'),
    path('companyapp/', CompanyAppListCreateView.as_view({'get': 'list', 'post': 'create'}), name='company_app_list_create'),
    path('companyapp/<pk>/', CompanyAppRetrieveUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name='company_app_retrieve_update'),
    path('job/', JobListCreateView.as_view({'get': 'list', 'post': 'create'}), name='job_list_create'),
    path('job/<pk>/', JobRetrieveUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name='job_retrieve_update')
]