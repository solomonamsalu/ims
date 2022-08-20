from django.db import models

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    reorder_level=models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):

        if self.quantity < self.reorder_level:
            # notify
            pass
        return super().save(*args, **kwargs)