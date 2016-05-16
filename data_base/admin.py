from django.contrib import admin

# Register your models here.
from data_base.models import data_basedata, Pkg, Proglam, Function

# Register your models here.
class data_basedataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date',)
    list_display_links = ('id', 'title',)
admin.site.register(data_basedata, data_basedataAdmin)


class PkgAdmin(admin.ModelAdmin):
    list_display = ('name', 'child', 'maker', 'tag',)
    list_display_links = ('name',)
admin.site.register(Pkg, PkgAdmin)


class ProglamAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'child', 'maker', 'tag',)
    list_display_links = ('name',)
admin.site.register(Proglam, ProglamAdmin)


class FunctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'maker', 'tag',)
    list_display_links = ('name',)
admin.site.register(Function, FunctionAdmin)
