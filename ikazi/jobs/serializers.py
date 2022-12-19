from rest_framework import serializers, viewsets
from .models import job,categories
from rest_framework.serializers import IntegerField
from .models import job
from datetime import date, timedelta
class JobSerializer(serializers.ModelSerializer):
    days_Published = serializers.SerializerMethodField('get_days_published')
    class Meta:
        model = job
        fields = (
            'job_id',
            'job_title',
            'job_type',
            'company',
            'Company_logo',
            'location',
            'experience',
            'category',
            'days_Published',
            'job_description',
        )
    def get_days_published(self, job):
        initial_day = job.date_posted
        today_date = date.today()
        days_ = today_date -initial_day
        days_Published = days_.days
        print(today_date, initial_day)
        return days_Published
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'

