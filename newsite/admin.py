from django.contrib import admin

# Register your models here.

from .models import AttTable, ReviewTable, TypeTable, UserTable, KeywordTable

admin.site.register(AttTable)
admin.site.register(ReviewTable)
admin.site.register(TypeTable)
admin.site.register(UserTable)
admin.site.register(KeywordTable)
