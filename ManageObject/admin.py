from django.contrib import admin
from .models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("pk", "firstName", "lastName", "slug", "password", "email", "slug")
    prepopulated_fields = {"slug" : ("firstName", "lastName")}
admin.site.register(Member, MemberAdmin)

class ListAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "date", "member")
    prepopulated_fields = {"slug" : ("title",)}
admin.site.register(List, ListAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "number", "list")
admin.site.register(Product, ProductAdmin)