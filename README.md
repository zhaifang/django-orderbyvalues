# django-orderbyvalues
一个django的猴子补丁，为QuerySet添加按照指定值进行排序的功能。

## 安装方式
1. git clone git@github.com:zhaifang/django-orderbyvalues.git
2. cd django-orderbyvalues
3. python3 setup.py build
4. python3 setup.py install

## 使用方式
1. import django-orderbyvalues
2. queryset.order_by_values(field_name, values)

## 例子
### model
```
from django.db import models 

class User(models.Model):
    name = models.CharField(max_length=255, db_index=True)
```
###按照指定名字顺序排序
```
User.objects.all().order_by_values('name', ['Alice', Bob', 'Eve'])
```

###此查询经过orm层的转换成的sql语句为

```
SELECT 
    (Field(name, "Bob", "Eve", "Alice")) AS "ordering_values", "id", "name" 
    ORDER BY "ordering_values" ASC;
```
