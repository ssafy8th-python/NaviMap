from django.db import models
from django.conf import settings
from navi_backend.themes.models import Theme, Tag

class Place(models.model):
    themes = models.ManyToManyField(Theme, through="Place_Theme", related_name="places")
    kakao_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    x_label = models.FloatField()
    y_label = models.FloatField()

class Place_Theme(models.model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    
    
class Review(models.model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    content = models.TextField()
    img_path = models.ImageField(blank=True, null=True)




