from django.db import models

# Create your models here.
from healthapp.utils.models import BaseModel


class news(BaseModel):
    news_type = (
        (0, '营养'),
        (1, '疾病'),
        (2, '知道'),
        (3, '两性'),
        (4, '运动'),
        (5, '减肥'),
        (6, '母婴'),
        (7, '中医'),
        (8, '心理'),
    )
    title = models.CharField(max_length=128, verbose_name="资讯标题")
    news_img = models.ImageField(upload_to="news", max_length=255, verbose_name="封面图片", default='icon/default.png',blank=True, null=True)
    checked = models.IntegerField(verbose_name='阅读量')
    catagorys = models.SmallIntegerField(choices=news_type, default=0, verbose_name="资讯分类")
    recommended = models.BooleanField(default=False, verbose_name='是否推荐')

    class Meta:
        db_table = "news"
        verbose_name = "资讯"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.title

    def catagory_name(self):
        # 返回资讯类型的中文
        return self.get_catagorys_display()


class news_detail(BaseModel):
    title = models.CharField(max_length=128,verbose_name='文章标题')
    author = models.CharField(max_length=32,verbose_name='作者名')
    article = models.TextField(verbose_name='文章内容')
    date = models.DateTimeField(verbose_name='发布时间')
    news_detail_img = models.ImageField(upload_to="courses", max_length=255, verbose_name="封面图片", default='icon/default.png',blank=True, null=True)

    thumbup = models.IntegerField(verbose_name='点赞数')

    class Meta:
        db_table = "news_detail"
        verbose_name = "资讯详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.title



class comment(BaseModel):
    username = models.CharField(max_length=32,verbose_name='评论用户')
    usericon = models.ImageField(upload_to='icon', default='icon/default.png',verbose_name='用户头像')

    content = models.CharField(verbose_name='评论内容', max_length=255)
    cmt_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    cmt_thumbup = models.IntegerField(verbose_name='评论点赞数')
    # 自关联
    parent = models.ForeignKey(to='self', null=True,on_delete=models.CASCADE)  # 有些评论就是根评

# {
#     "username":"laoba",
#     "usericon":"http://127.0.0.1:8000/media/icon/default.png",
#     "content":"11111123232",
#     "cmt_time":1231,
#     "cmt_thumbup":109
# }