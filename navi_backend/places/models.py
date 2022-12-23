from django.db import models
from django.conf import settings
from themes.models import Theme, Tag

class Place(models.Model):
    themes = models.ManyToManyField(Theme, through="Place_Theme", related_name="places")
    kakao_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    x_label = models.FloatField()
    y_label = models.FloatField()

class Place_Theme(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)    
    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    content = models.TextField()
    emoticon = models.CharField(max_length=100)
    img_path = models.ImageField(blank=True, null=True)




