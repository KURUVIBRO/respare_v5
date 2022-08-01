from django.db import models
from django.conf import settings
# Create your models here.
class Topic(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=500)
    image=models.URLField(max_length=200,default=None)
    wide_image=models.URLField(max_length=200,default=None)
    def __str__(self)->str:
        return str(self.id)+'.  '+self.title

class Choice(models.Model):
    class Meta:
        unique_together=(('topic','option_no'))
    id=models.IntegerField(primary_key=True)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    option_no=models.IntegerField(default=0)
    option=models.CharField(max_length=55)
    count=models.IntegerField(default=0)
    def __str__(self)->str:
        return str(self.id)+'.  '+self.option+'  '+str(self.topic)

class Reaction(models.Model):
    class Meta:
        unique_together=(('user','choice','topic'))
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    time=models.DateTimeField()
    