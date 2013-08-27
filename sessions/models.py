from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Session(models.Model):
    title = models.CharField(max_length=250)
    submitters = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title
