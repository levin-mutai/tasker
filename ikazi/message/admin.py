from django.contrib import admin
from .models import Client_messages
# Register your models here.
admin.site.site_header  =  "IkokaziKenya"
admin.site.site_title  =  "IkokaziKenyae"
admin.site.index_title  =  "IkokaziKenya"
admin.site.register(Client_messages)
