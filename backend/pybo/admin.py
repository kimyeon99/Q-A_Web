from django.contrib import admin
from .models import Question

# subject로 검색 가능 기능 추가
# 장고 관리자의 기능 중 하나
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

class QustionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QustionAdmin)
