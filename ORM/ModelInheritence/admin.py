from django.contrib import admin

from ModelInheritence.models import ContactInfo1,Student,Student1,Teacher,Teacher1,Child1,Parent2,Parent1,SubChild,Child,Parent
# Register your models here.
admin.site.register(ContactInfo1)
admin.site.register(Student)
admin.site.register(Student1)
admin.site.register(Teacher)
admin.site.register(Teacher1)
admin.site.register(Parent1)
admin.site.register(Child1)
admin.site.register(Parent2)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SubChild)