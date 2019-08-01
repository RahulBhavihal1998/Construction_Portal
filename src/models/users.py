from django.db import models


class site(models.Model):
    id              = models.AutoField(primary_key=True)
    site_name       = models.CharField(max_length=50, default="N/A")
    site_location   = models.CharField(max_length=50, default="N/A")
    site_area       = models.BigIntegerField(default=1200)
    site_cost       = models.BigIntegerField(default=50000)
    email_id        = models.CharField(max_length=100, default="")
    password        = models.CharField(max_length=18, default="")
    salt            = models.CharField(max_length=64, default="")

    def save(self, *args, **kwargs):
        return super(site, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'table'
        app_label = 'src'
