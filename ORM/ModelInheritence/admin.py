from django.contrib import admin

from ModelInheritence.models import ContactInfo1,Student,Student1,Teacher,Teacher1
# Register your models here.
admin.site.register(ContactInfo1)
admin.site.register(Student)
admin.site.register(Student1)
admin.site.register(Teacher)
admin.site.register(Teacher1)