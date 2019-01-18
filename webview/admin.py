from django.contrib import admin
from webview.models import pvrusers, citites, movie

class cititesAdmin(admin.ModelAdmin) :
    list_display = []

    for columnName in citites._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

admin.site.register(citites,cititesAdmin)

class pvrusersAdmin(admin.ModelAdmin) :
    list_display = []

    for columnName in pvrusers._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

admin.site.register(pvrusers,pvrusersAdmin)

class movieAdmin(admin.ModelAdmin) :
    list_display = []

    for columnName in citites._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

admin.site.register(movie,movieAdmin)
# Register your models here.
