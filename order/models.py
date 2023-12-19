from django.db import models

# Create your models here.

class Test(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="test")
    def __str__(self):
        return self.name
    
    
class DishCategory(models.Model):
    Id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, verbose_name="菜品种类")
    type = models.CharField(max_length=100, verbose_name="type",default="")


    sort_order = models.IntegerField(default=0, verbose_name="排序")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "菜品种类"
        verbose_name_plural = verbose_name


class DishManagement(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="菜品名称")

    Dishclass = models.ForeignKey(
        DishCategory,
        on_delete=models.CASCADE,
        verbose_name="菜品种类",
        related_name="pk_Dishclass",
        null=True,
    )
    # pacakge = models.FileField(
    #     upload_to="test/file/", verbose_name="其他压缩包", blank=True, null=True
    # )  # 文件上传字段
    # DishCategoryList = models.ManyToManyField(DishCategory)

    Dishimage = models.ImageField(
        max_length=100,
        verbose_name="菜品图片",
        upload_to="Dishimage/%Y/%m/%d/",
        null=True,
        blank=True,
    )
    inventory = models.IntegerField(default=0, verbose_name="库存")
    price = models.IntegerField(default=0, verbose_name="价格")
    sort = models.IntegerField(default=0, verbose_name="排序")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "菜品管理"
        verbose_name_plural = verbose_name
