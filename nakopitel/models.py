from django.db import models
class Price(models.Model):
    category_of_prisoed_mosh = models.PositiveSmallIntegerField()
    category = models.PositiveSmallIntegerField()
    title ="Категория: "+str(category)+"Категория присоединенной мощности: "+str(category_of_prisoed_mosh)
    chas0 = models.FloatField()
    chas1 = models.FloatField()
    chas2 = models.FloatField()
    chas3 = models.FloatField()
    chas4 = models.FloatField()
    chas5 = models.FloatField()
    chas6 = models.FloatField()
    chas7 = models.FloatField()
    chas8 = models.FloatField()
    chas9 = models.FloatField()
    chas10 = models.FloatField()
    chas11 = models.FloatField()
    chas12 = models.FloatField()
    chas13 = models.FloatField()
    chas14 = models.FloatField()
    chas15 = models.FloatField()
    chas16 = models.FloatField()
    chas17 = models.FloatField()
    chas18 = models.FloatField()
    chas19 = models.FloatField()
    chas20 = models.FloatField()
    chas21 = models.FloatField()
    chas22 = models.FloatField()
    chas23 = models.FloatField()
    price_po_chas=[chas0,chas1,chas2,chas3,chas4,chas5,chas6,chas7,chas8,chas9,chas10,chas11,chas12,chas13,chas14,chas15,chas16,chas17,chas18,chas19,chas20,chas21,chas22,chas23]

    def __str__(self):
        return self.title
# Create your models here.

# Create your models here.
