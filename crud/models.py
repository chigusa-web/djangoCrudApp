from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=200, verbose_name="商品名")
    price = models.IntegerField(verbose_name="価格")

    def __str__(self):
        return self.name

    # 新規登録・編集完了後のリダイレクト先
    def get_absolute_url(self):
        return reverse('crud:list')
