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
    birthday=models.DateField(default='1900-01-01',verbose_name='年龄')
    sex=models.CharField(max_length=6,choices=sex,default='female',verbose_name='性别')
    location=models.CharField(max_length=10,choices=location,default='火星',verbose_name='居住地')
    avatars=models.CharField(max_length=256,verbose_name='头像')
    # 建立表连接，一对一关系
    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


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

class Profile(models.Model):
    '''个人资料'''
    sex = (
        ('man', '男'),
        ('featle', '女'),
    )
    location = (
        ('北京', '北京'),
        ('南京', '南京'),
        ('上海', '上海'),
        ('安徽', '安徽'),
    )
    dating_gender = models.CharField(max_length=6, choices=sex, default='male', verbose_name='匹配的性别')
    dating_location = models.CharField(max_length=15, choices=location, default='上海', verbose_name='目标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')

    def to_dict(self):
        return {
            'id': self.id,
            'dating_gender': self.dating_gender,
            'dating_location': self.dating_location,
            'min_distance': self.min_distance,
            'max_distance': self.max_distance,
            'min_dating_age': self.min_dating_age,
            'max_dating_age': self.max_dating_age,
            'vibration': self.vibration,
            'only_matche': self.only_matche,
            'auto_play': self.auto_play,
        }

