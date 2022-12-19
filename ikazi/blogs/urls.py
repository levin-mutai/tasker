from django.urls import include,path,re_path

from .routers import blogs,popularBlogs

urlpatterns = [
    path('',include(blogs.urls)),
    path('popular/',include(popularBlogs.urls))
]