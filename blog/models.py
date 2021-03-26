from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:120] + "...."

    def __str__(self):
        return self.title