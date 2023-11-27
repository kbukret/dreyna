from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)


# Register your models here.
admin.site.site_header = 'Dr. Solutions'
admin.site.index_title = 'Panel de control DR.SOLUTIONS'
admin.site.site_title = 'DrSolutions'
