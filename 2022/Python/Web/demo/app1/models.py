from django.db import models        # 引入Django.db.models模块

# Create your models here.
class CreateUpdate(models.Model):   # 创建抽象数据类型，同样要继承于models.Model
    # 创建时间，使用models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间，使用models.DateTimeField
    updated_at = models.DateTimeField(auto_now=True)


class Meta:     # 元数据，除了字段以外的所有属性
    # 设置model为抽象类，指定该表不应该在数据库中创建
    abstract = True


class Person(CreateUpdate):     # 继承CreateUpdate类
    """
    编写Person模型类，数据模型应该继承于models.Model或其子类
    """
    # 第一个字段使用models.CharField类型
    first_name = models.CharField(max_length=30)
    # 第二个字段使用models.CharField类型
    last_name = models.CharField(max_length=30)


class Order(CreateUpdate):      # 继承CreateUpdate类
    order_id = models.CharField(max_length=30, db_index=True)
    order_desc = models.CharField(max_length=120)