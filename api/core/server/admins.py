# coding: utf-8
from django.contrib import admin

from core.database.models import FilteredMultiSelectField


class BaseModelAdmin(admin.ModelAdmin):
    # 分页显示，一页的数量
    list_per_page = 10

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, FilteredMultiSelectField):
            # 必须定义获取该字段数据的方法, 方法返回queryset对象, 格式get_+字段名
            queryset_call = getattr(self, 'get_select_{}'.format(db_field.name))
            kwargs['queryset'] = queryset_call(db_field, request, **kwargs)
            return db_field.formfield(**kwargs)
        else:
            form_field = super(BaseModelAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)
            return form_field

