from django.contrib import admin

# Register your models here.
from .models import Address, Student, Address2, Student2, Club

admin.site.register(Address)
admin.site.register(Student)
admin.site.register(Address2)
admin.site.register(Student2)
admin.site.register(Club)