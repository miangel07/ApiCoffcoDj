from django.db import models

class RolModels(models.Model):
    rol=models.CharField(max_length=150)

    def __str__(self):
        return self.rol