from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)    
    ski_area = models.CharField(max_length=100, default='Park City Mountain Resort')
    base = models.CharField(max_length=100, default='Canyons')
    epic_PassNumber = models.BigIntegerField(null=True, verbose_name='Passnumber list on the Epic Mix app.')
    physical_PassNumber = models.BigIntegerField(null=True, verbose_name='Passnumber listed on your printed Epic pass.')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.ski_area}"
