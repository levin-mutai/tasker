from rest_framework import serializers
from .models import Blogs

class BlogsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

class PopularBlog(serializers.ModelSerializer):
    class Meta:
        fields = (
            'blog_id',
            'blog_image',
            'blog_title',
            'blog_slug',
            'content',
            'views',
            'rating',
            'date_posted',
            'minute_read'
        )
        model = Blogs

