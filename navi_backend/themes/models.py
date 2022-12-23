from django.db import models
from django.conf import settings


class Tag(models.Model):
    tag_name = models.CharField(max_length=45)


class Theme(models.Model):
    theme_title = models.CharField(max_length=200)
    
    # 작성자만 수정 가능하도록 default를 0으로 설정하였습니다.
    is_update = models.BooleanField(default=0)  

    theme_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    theme_tags = models.ManyToManyField(Tag, related_name="tag_themes")
    created = models.DateTimeField(auto_now_add=True)

    # 좋아요 한 유저가 담겨있습니다.
    theme_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_themes_likes')
