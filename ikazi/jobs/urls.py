from django.urls import path,re_path,include
from .views import jobListAPIView,SingleJobListAPIView,SearchJobListView,VacancyByCategories
from .router import JobCategory,singlejobs
urlpatterns =[
    path('jobs/',jobListAPIView.as_view()),
    # re_path('^jobs/(?P<job_id>.+)/$', SingleJobListAPIView.as_view()),
    path('',include(JobCategory.urls)),
    path('',include(singlejobs.urls)),

    path('vacancies',VacancyByCategories.as_view()),
    #------------------------------------------------------------------------------------------------
            #job search urls
    #------------------------------------------------------------------------------------------------
    re_path('^search-jobs/(?P<location>.+)/$', SearchJobListView.as_view(), {'category': None}),
    re_path('^search-jobs/(?P<category>.+)/(?P<location>.+)$', SearchJobListView.as_view()),
    re_path('^search-jobs/(?P<category>.+)/$', SearchJobListView.as_view(), {'location': None}),
    re_path('^search-jobs/', SearchJobListView.as_view(), {'category': None,'location': None}),

]
