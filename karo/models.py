from django.db import models
from django.utils import timezone




# Create your models here.

CHOICE = (("secondary", "NIGHT"), ("primary", "DAYTIME"), ("danger", "MORNING"))

def ten():
    pkpk=KaroModel.objects.get(pk=84).goleKcol
    return pkpk


class KaroModel(models.Model):
    eat = models.CharField(max_length=20)
    kcol = models.IntegerField(null=True, blank=True, default=0)
    daycolor = models.CharField(
        max_length=10,
        choices = CHOICE,
        default = "secondary"
        )

    date = models.DateTimeField(default=timezone.now())
    goleKcol = models.IntegerField(default=0)

    def __str__(self):
        return self.eat