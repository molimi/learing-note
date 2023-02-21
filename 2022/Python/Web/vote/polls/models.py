# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Subject(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    is_hot = models.BooleanField(verbose_name='是否热门')

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        verbose_name_plural = '学科'
        db_table = 'tb_subject'


class Teacher(models.Model):
    sex_choices = (
        (0, '女'),
        (1, '男'),
    )
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.SmallIntegerField(default=1, verbose_name='性别', choices=sex_choices)
    birth = models.DateField(verbose_name='出生日期')
    intro = models.CharField(max_length=1000, verbose_name='个人介绍')
    photo = models.ImageField(max_length=255, verbose_name='照片')
    gcount = models.IntegerField(default=0, db_column='gcount', verbose_name='好评数')
    bcount = models.IntegerField(default=0, db_column='bcount', verbose_name='差评数')
    sno = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='所属学科', db_column='sno')

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        verbose_name_plural = '老师'
        db_table = 'tb_teacher'
