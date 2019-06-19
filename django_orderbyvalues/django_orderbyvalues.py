# -*- coding: utf-8 -*-

from django.db.models.query import QuerySet


# 猴子补丁，为queryset增加按照指定值排序的功能
def order_by_values(self, field, values, temp_name='ordering_values'):
    if field == 'pk':
        field = self.model._meta.db_table + '.' + self.model._meta.pk.name
    value_list = ', '.join(['"%s"' % value if isinstance(value, str) else value for value in values])
    sql = 'FIELD(%s, %s)' % (field, value_list)
    return self.extra(select={temp_name: sql}, order_by=(temp_name,))


# 为默认的queryset添加新方法
QuerySet.order_by_values = order_by_values
