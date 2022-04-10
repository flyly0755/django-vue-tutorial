from django.contrib import admin
from django import forms

from django_admin_hstore_widget.forms import HStoreFormField
# Register your models here.


from .models import Type, Label, Misc, MovieBaseInfo, MovieBoNewsInfo

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'typename', 'created']



@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'labelname', 'created']

@admin.register(Misc)
class MiscAdmin(admin.ModelAdmin):
    list_display = ['id', 'miscname', 'created']



class MovieBaseInfoAdminForm(forms.ModelForm):
    director = HStoreFormField()

    class Meta:
        model = MovieBaseInfo
        exclude = ()

@admin.register(MovieBaseInfo)
class MovieBaseInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'moviename', 'xpname', 'director']
    form = MovieBaseInfoAdminForm

