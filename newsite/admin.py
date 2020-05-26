from django.contrib import admin

# Register your models here.

from .models import AttTable1, ReviewTable, TypeTable, UserTable, KeywordTable

admin.site.register(AttTable1)
admin.site.register(ReviewTable)
admin.site.register(TypeTable)
admin.site.register(UserTable)
admin.site.register(KeywordTable)
