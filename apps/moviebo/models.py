from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.contrib.postgres.fields import HStoreField
from mdeditor.fields import MDTextField



class Label(models.Model):
    """电影标签"""
    labelname = models.CharField(max_length=16, unique=True, verbose_name="电影标签")
    created = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = "电影标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.labelname


class Type(models.Model):
    """电影类型"""
    typename = models.CharField(max_length=16, unique=True, verbose_name="电影类型")
    created = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = "电影类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.typename

class Misc(models.Model):
    """电影属性"""
    miscname = models.CharField(max_length=16, unique=True, verbose_name="电影属性")
    created = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = "电影属性"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.miscname


# class MovieAvatar(models.Model):
#     content = models.ImageField(upload_to='avatar/%Y%m%d')


class MovieBaseInfo(models.Model):
    '''影片基本信息'''
    moviename = models.CharField(max_length=32, null=False, blank=False, verbose_name="中文片名")
    xpname = models.CharField(max_length=32, null=False, blank=False, verbose_name="中文非重复片名",
                              unique=True)
    # director = ArrayField(models.CharField(max_length=16), verbose_name='导演')
    director = HStoreField(verbose_name='导演')
    # actor = ArrayField(models.CharField(max_length=16), verbose_name='演员')
    brief_intro = models.TextField(default="", verbose_name='剧情简介', null=True, blank=True, help_text='剧情简介')
    jsondetailinfo = JSONField(null=True, blank=True, verbose_name='影片json信息')  # 非结构化字段信息
    actordetail = JSONField(null=True, blank=True, verbose_name='演员信息')
    # labels = ArrayField(models.ForeignKey(Lable, null=True, blank=True, on_delete=models.SET_NULL,
    #                                       related_name='movie_label'))
    movieavatar = models.ImageField(upload_to='avatar/%Y%m%d', null=True, blank=True, verbose_name='电影海报')
    labels = models.ManyToManyField(Label, blank=True, verbose_name='电影标签')
    types = models.ManyToManyField(Type, blank=True, verbose_name='电影类型')
    miscs = models.ManyToManyField(Misc, blank=True, verbose_name='电影属性')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = "影片基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.moviename


class MovieBoNewsInfo(models.Model):
    title = models.CharField(max_length=64, null=True, blank=True, verbose_name="票房资讯标题", unique=True)
    content = MDTextField(max_length=5000, verbose_name="票房资讯正文")
    relatedmovie = models.ManyToManyField(MovieBaseInfo, blank=True)
    hiddenflg = models.BooleanField(default=False)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = "票房资讯"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title