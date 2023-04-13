from django.contrib import admin
from .models import Hotels, Freatures
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin


# Register your models here.
# class HotelsResource(resources.ModelResource):
#     class Meta:
#         model = Hotels


# class HotelAdmin(ImportExportModelAdmin):
#     resource_class = HotelsResource


admin.site.register(Freatures)
admin.site.register(Hotels)


