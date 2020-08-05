from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length= 30)
    desc= models.CharField(max_length= 230)
    image= models.ImageField(upload_to='myportfolio/images/')
    url= models.URLField(blank=True)

    def __str__(self):
        return self.title
