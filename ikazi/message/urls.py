from django.urls import include,path,re_path

from .views import MessageCreateViewset,SubscribeCreateViewset

urlpatterns = [
    path('messages/', MessageCreateViewset.as_view()),
    path('subscribe/',SubscribeCreateViewset.as_view())
]

