from django.db import models

# Create your models here.

class Shop(models.Model):
    #店家名稱
    shopname = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ")" + self.shopname
    
class Option(models.Model):
    #屬於哪一家店
    shop_id = models.IntegerField()
    #選項文字
    drinkname = models.CharField(max_length=50)
    #被訂購數
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.shop_id) + "： " + self.drinkname
        
