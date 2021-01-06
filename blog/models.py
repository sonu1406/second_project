from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=250)
    pub_date=models.TimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
