from django.db import models
from django.utils import timezone
# Create your models here.

CHOICE = (("secondary", "NIGHT"), ("primary", "DAYTIME"), ("danger", "MORNING"))

class KaroModel(models.Model):
    #食べたもの
    eat = models.CharField(max_length=20)
    #食べたもののカロリー
    kcol = models.IntegerField(null=True, blank=True, default=0)
    #食べた時間帯（朝、昼、夜）
    daycolor = models.CharField(
        max_length=10,
        choices = CHOICE,
        default = "secondary"
        )
    #食べた時間
    date = models.DateTimeField(default=timezone.now())
    #目標カロリーの設定
    goleKcol = models.IntegerField(default=0)

    def __str__(self):
        return self.eat