from rest_framework import routers

from .views import CategorJobListingView,SingleJobListAPIViewset

JobCategory = routers.DefaultRouter()
JobCategory.register('job-category',CategorJobListingView, basename='Job Category')

singlejobs = routers.DefaultRouter()
singlejobs.register('jobs',SingleJobListAPIViewset,basename="single job")