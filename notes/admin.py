from django.contrib import admin

# Register your models here.
from . models import *
admin.site.register(StudyMaterial)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Semisters)
admin.site.register(StudyMaterialTypes)