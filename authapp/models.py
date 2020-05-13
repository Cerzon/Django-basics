from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class HoHooUser(AbstractUser):
    userpic = models.ImageField(upload_to='userpic/', blank=True, verbose_name='аватар')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='отчество')
    occupation = models.CharField(max_length=60, blank=True, verbose_name='должность')
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        result = '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)
        return result.strip()

    @property
    def short_name(self):
        result = '{} {}'.format(self.first_name, self.last_name)
        return result.strip()

    def quote(self):
        result = self.quotes.filter(product__isnull=True).order_by('?')
        if result:
            result = result[0]
        return result
