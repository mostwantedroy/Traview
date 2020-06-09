from django.contrib import admin

# Register your models here.

from .models import *


class AttTableAdmin(admin.ModelAdmin):
    model = AttTable
    list_display = ('type', 'id', )
    search_fields = ('type__detail_code', 'id__id')

class CodeTableAdmin(admin.ModelAdmin):
    model = CodeTable
    list_per_page = 25
    list_display = ('detail_code', 'code', 'detail_name', )
    search_fields = ('detail_code', 'code', 'detail_name', )

class KeywordTableAdmin(admin.ModelAdmin):
    model = KeywordTable
    list_display = ('id', 'valuation', 'view', 'cost', 'total', )
    search_fields = ('id', 'valuation', 'view', 'cost', 'total', )

admin.site.register(AttTable, AttTableAdmin)
admin.site.register(ReviewTable)
admin.site.register(UserTable)
admin.site.register(CodeTable, CodeTableAdmin)
admin.site.register(ChoiceTable)
admin.site.register(CodeDef)
admin.site.register(KeywordTable, KeywordTableAdmin)