from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
admin.site.site_title = "订餐系统"
admin.site.site_header = "订餐系统"
@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
  
    list_display = (
        "Id",
        "name",
        "sort_order",
        "created_at",
       
    )  
    search_fields = ("Id", "name")   
    exclude = []


    # # 增加自定义按钮
    # actions = ['make_copy', 'custom_button']
    # def custom_button(self, request, queryset):
    #     print(request, queryset)

    # # 显示的文本，与django admin一致
    # custom_button.short_description = ' 打印'
    # # icon，参考element-ui icon与https://fontawesome.com
    # custom_button.icon = 'fas fa-print'

    # # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    # custom_button.type = 'primary'

    # # 给按钮追加自定义的颜色
    # custom_button.style = 'color:black;'



@admin.register(Test)

class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(DishManagement)
class DishManagementAdmin(admin.ModelAdmin):
  
    list_display = (
        "Id",
        "name",
        "Dishclass",
        
               "inventory",
        "price",
        "sort",
        "Dishimage_",

    )  
    def Dishimage_(self, obj):
        if obj.Dishimage:
            return format_html('<a href="{}"><img src="{}" style="height:80px;"/></a>', obj.Dishimage.url,obj.Dishimage.url)
        else:
            return "-"

    Dishimage_.short_description = format_html(
        '<a id="huangchengwu" href="?o=4">图片</a>')
    Dishimage_.allow_tags = True
    search_fields = ("Id", "name" ,"inventory","price","sort")   
    exclude = []

 


