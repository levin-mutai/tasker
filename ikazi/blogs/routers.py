from rest_framework import routers

from .views import BlogsViewSet,PopularBlogViewSet

blogs = routers.DefaultRouter()
blogs.register('blogs', BlogsViewSet, basename='Blogs')

popularBlogs = routers.DefaultRouter()
popularBlogs.register('blogs',PopularBlogViewSet, basename='popular blog')


