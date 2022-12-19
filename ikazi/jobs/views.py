from django.shortcuts import render
from rest_framework import routers,viewsets,generics,status
from rest_framework.response import Response

from .serializers import JobSerializer,CatSerializer
from .models import job,categories
# Create your views here.


class jobListAPIView(generics.ListAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer

class SingleJobListAPIView(generics.ListAPIView):
    '''
    Used to get specific job listing using their job id. Pass the id at the end of the url eg http://127.0.0.1:8001/api/jobs/3/ where '3' is the job id. Ensure to add the '/' at the end of the url endpoint to avoid getting errors.
    The data returned
    '''
    queryset = job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'job_id'

    def get_queryset(self):
        jobs = self.kwargs.get('job_id')
        specific_job = job.objects.filter(job_id=int(jobs))
        return specific_job

    def get(self, request, *args, **kwargs):
        try:
            data = JobSerializer(self.get_queryset(),many=True).data
            assert data
            print(data)
            context = {
                'data': data,
                'success': True,
                'status': status.HTTP_200_OK
                }
            return Response(context,context={"request":
                      request},content_type='json')
        except Exception as err:
            context = {'error': str(err) if str(err) else "job not found", 'success': "false", 'messages': 'Failed To Get jobs.'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleJobListAPIViewset(viewsets.ModelViewSet):
    '''
    Used to get specific job listing using their job id. Pass the id at the end of the url eg http://127.0.0.1:8001/api/jobs/3/ where '3' is the job id. Ensure to add the '/' at the end of the url endpoint to avoid getting errors.
    The data returned
    '''
    queryset = job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ['get','options', 'head']
    lookup_field = 'job_id'

    def get_queryset(self):
        specific_job = job.objects.all()
        return specific_job

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        data = job.objects.filter(job_id=int(params['job_id']))
        seralizer = JobSerializer(data,context={"request":
                      request},many=True)
        context = {
            'data': seralizer.data,
            'success': True,
            'status': status.HTTP_200_OK
        }
        return Response(seralizer.data)

class CategorJobListingView(viewsets.ModelViewSet):
    '''
    used to filter jobs using the required category. This will return all the jobs in the required categories.
    '''
    queryset = job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        specific_job = job.objects.all()
        return specific_job

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        queryset = job.objects.filter(category = params['pk'])
        serializer = JobSerializer(queryset, many=True)
        context = {
            'data': serializer.data,
            'success': True,
            'status': status.HTTP_200_OK
        }
        return Response(context, status=status.HTTP_200_OK) if serializer.data else Response(
            {'error': 'Blog not found', 'success': False, 'status': status.HTTP_404_NOT_FOUND},
            status=status.HTTP_404_NOT_FOUND)

        
class SearchJobListView(generics.ListAPIView):
    '''
    used to search jobs using location and category or either location only or category only.
    '''
    queryset = job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        category = self.kwargs.get('category')
        location = self.kwargs.get('location')
        if category and location:
            specific_job = job.objects.filter(category=category, location=location)
        elif category and not location :
            specific_job = job.objects.filter(category=category)
        elif location and not category :
            specific_job = job.objects.filter(location=location)
        else:
            specific_job = job.objects.all()

        return specific_job

    def get(self, request, *args, **kwargs):
        try:
            data = JobSerializer(self.get_queryset(), many=True).data
            assert data
            context = {
                'data': data,
                'success': True,
                'status': status.HTTP_200_OK
            }
            return Response(context, content_type='json')
        except Exception as err:
            context = {'error': str(err) if str(err) else "job not found", 'success': "false",
                       'messages': 'Failed To Get jobs.'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VacancyByCategories(generics.ListAPIView):
    '''
    used to get all the vacancies in every CATEGORY
    '''
    categories = categories.objects.all()
    queryset = job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'job_id'

    def get_queryset(self):
        cat = categories.objects.all()
        return cat

    def get(self, request, *args, **kwargs):
        try:
            data = CatSerializer(self.get_queryset(),many=True).data
            assert data
            allCategories = self.get_queryset().values()
            categori = list({})
            for i in allCategories:
                categoryVacancy = {'category':i['jcategory'],"vacancy":job.objects.filter(category=i['jcategory']).count()}
                categori.append(categoryVacancy)
            context = {
                'data': categori,
                'success': True,
                'status': status.HTTP_200_OK
                }
            return Response(context,content_type='json')
        except Exception as err:
            context = {'error': str(err) if str(err) else "job not found", 'success': "false", 'messages': 'Failed To Get jobs.'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 