from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # 关联User App
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """具体知识"""
    # 主表数据删除其他一并删除
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(str(self.text)) > 50:
            return self.text[:50] + str('...')
        else:
            return self.text