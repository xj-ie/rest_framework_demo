# rest_framework_demo
django-演示教学

## １、序列化与反序列化



![image-20200819203435060](/home/python/Desktop/rest_framework/rest_framework_demo/image/image-20200819203435060.png)

修改添加模型类序列字段与属性

## ２、rest视图

##### rest 的APIView继承了Django的View类新增权限、认证、限流等功能

​	限流：是指限制用户访问次数来防止爬虫程序来爬去网页信息等

##### GenericAPIview与API一样是rest的视图类，他是继承了rest的ＡＰＩVeiw类新增了分页，过滤排序、指定查询集。	

​	queryset＝查询集

##### 可以指定序列化器到属性中去。

​	　serialzier_class＝序列化器

## ３、拓展类　

##### 　一共有五个拓展类，需要配合ＧenericＡＰＩＶiew使用

​	ListModelMixin	获取多少个数据对象　　

​	CreateModelMixin	保存数据　

​	RetrieveModelMxin	获取单一数据对象　	　　　　

​	UpdateModelMixin	更新数据　

​	DestroyModelMixin 	删除数据　