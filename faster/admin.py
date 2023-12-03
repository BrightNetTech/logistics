from django.contrib import admin
from faster.models import Contact, Service, Comment



admin.site.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Subject' 'Message']

admin.site.register(Service)
class Service(admin.ModelAdmin):
    list_display = ['Customer Name', 'Origin', 'Destination' 'Email', 'Payment' 'Service']


admin.site.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Subject' 'Message']

# Register your models here.
    