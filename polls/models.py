import datetime


from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 如果要把一个类的实例变成 str，就需要实现特殊方法__str__
    #这么做不仅仅是为了在交互界面方便
    # 更重要的是在django中这种对象描述的方式到处都是

    def __str__(self):
        return self.question_text

    # 打印当前的时间

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # ...

    def __str__(self):
        return self.choice_text