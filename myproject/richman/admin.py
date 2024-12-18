from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
from .models import *


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]

    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }


admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(Product, ProductAdmin)
