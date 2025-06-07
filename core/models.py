from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(("Name"), max_length=50)
    role1 = models.CharField(max_length=50)
    role2 = models.CharField(("role 2"), max_length=50)

    def __str__(self) -> str:
        return self.name
    
class About(models.Model):
    bd = models.DateField(("Birth Day"), auto_now=False, auto_now_add=False)
