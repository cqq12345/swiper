from django.db import models

# Create your models here.




# Create your models here

from django.db import models

class like(models.Model):
    sex=(
        ('man','男'),
        ('featle','女'),
    )
    location=(
        ('北京','北京'),
        ('南京','南京'),
        ('上海','上海'),
        ('安徽','安徽'),
         )

    uid=models.CharField(max_length=6,verbose_name='用户id')
    nickname=models.CharField(max_length=6,verbose_name='用户名')
    birthday=models.DateField(default='1900-0-0',verbose_name='年龄')
    sex=models.CharField(max_length=6,choices=sex,verbose_name='性别')
    location=models.CharField(max_length=10,choices=location,verbose_name='居住地')
    avatars=models.CharField(max_length=256,verbose_name='头像')



