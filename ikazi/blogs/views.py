from django.db.models import F
from django.shortcuts import render
from rest_framework import viewsets, generics,permissions,status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from .models import Blogs
from rest_framework.response import Response
from .serializers import BlogsSerializers,PopularBlog
# Create your views here.

class BlogsViewSet(viewsets.ModelViewSet):
    '''
    used to obtain both specific and all the blogs in the database ordered by ID. To obtain specific blog pass the blog id to the end point.
    '''
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializers
    http_method_names = ['get','head','options']
    # permission_classes = IsAuthenticatedOrReadOnly

    def get_queryset(self):
        specific_Blog = Blogs.objects.all()
        return  specific_Blog

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        queryset = Blogs.objects.filter(blog_id = params['pk'])
        serializer = BlogsSerializers(queryset,context={"request":
                      request},many=True)

        Blogs.objects.filter(pk=params['pk']).update(views=F('views') + 1)
        content = {
            'data': serializer.data,
            'success': True,
            'status': status.HTTP_200_OK
        }
        return Response(content, status=status.HTTP_200_OK) if serializer.data else Response({'error':'Blog not found','success': False, 'status': status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)

class PopularBlogViewSet(viewsets.ModelViewSet):
    '''
    This endpoint is used to obtain the popular blogs based on the number of views. The blog with more views will appear first followed by the others in decreasing order.
    To obtain number of popular blogs; eg 10 popular blogs, pass the number of popular blogs you would need to this end point. e.g. http://127.0.0.1:8001/api/popular/blogs/10/, where 10 is the number of blogs you would want to receive.
    '''
    queryset = Blogs.objects.all()
    serializer_class = PopularBlog
    http_method_names = ['get','head', 'options']

    # def get_queryset(self):
    #     specific_Blog = Blogs.objects.all().order_by('-views')
    #     serializer = PopularBlog(specific_Blog, many=True)
    #     context = {
    #         'data': serializer.data,
    #         'success': True,
    #         'status': status.HTTP_200_OK
    #     }
    #     print(specific_Blog)
    #     return context
    def get_queryset(self):
        specific_Blog = Blogs.objects.all().order_by('-views')

        return  specific_Blog

    def get(self, request, *args, **kwargs):
        try:
            data = BlogsSerializers(self.get_queryset(),many=True).data
            assert data
            context = {
                'data': data,
                'success': True,
                'status': status.HTTP_200_OK
                }
            return Response(context,content_type='json')
        except Exception as err:
            context = {'error': str(err) if str(err) else "job not found", 'success': "false", 'messages': 'Failed To Get jobs.'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        queryset = Blogs.objects.all().order_by('-views')[:int(params['pk'])]
        serializer = BlogsSerializers(queryset, many=True)
        context = {
            'data': serializer.data,
            'success': True,
            'status': status.HTTP_200_OK
        }
        return Response(context, status=status.HTTP_200_OK) if serializer.data else Response({'error': 'Blog not found', 'success': False, 'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

