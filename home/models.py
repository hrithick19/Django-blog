from django.db import models

class contactForm(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name

    