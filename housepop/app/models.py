from django.db import models
from django.contrib.auth.models import User
from tastypie.utils.timezone import now

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User)
    info = models.TextField()
    image_url = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=now)
    #is_active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.info
