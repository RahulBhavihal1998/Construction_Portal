from django.db import models
from src.models.users import site
import os, binascii
from rest_framework.authtoken.models import Token

TOKEN_LENGTH = 40

class TokenManager(models.Manager):
    def generate_access_token(self):
        return binascii.hexlify(os.urandom(TOKEN_LENGTH / 2)).decode()

class Token(models.Model):
    access_token = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(site)
    objects = TokenManager()

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = Token.objects.generate_access_token()
        return super(Token, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.access_token

    class Meta:
        db_table = 'token'
        app_label = 'src'

