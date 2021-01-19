from django.db import models
from django.conf import settings

# Create your models here.
class Password(models.Model):
    site_url = models.URLField(max_length=400)
    nick_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=2000)
    email = models.EmailField()
    phone = models.CharField(max_length=10,blank=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='master_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    models.UniqueConstraint(fields=[site_url,username],name='unique_login')
    def __str__(self):
        return self.nick_name
