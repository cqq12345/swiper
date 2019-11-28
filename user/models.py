from django.db import models

# Create your models here.




# Create your models here

from django.db import models

class User(models.Model):
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

    phonenum=models.CharField(max_length=15,unique=True,verbose_name='手机')
    nickname=models.CharField(max_length=6,default='匿名用户',verbose_name='用户名')
    birthday=models.DateField(default='1900-0-0',verbose_name='年龄')
    sex=models.CharField(max_length=6,choices=sex,default='female',verbose_name='性别')
    location=models.CharField(max_length=10,choices=location,default='火星',verbose_name='居住地')
    avatars=models.CharField(max_length=256,verbose_name='头像')

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'gender': self.sex,
            'birthday': str(self.birthday),
            'location': self.location,
            'avatar': self.avatars,
        }



