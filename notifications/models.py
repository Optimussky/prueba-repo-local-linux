from django.db import models
import uuid
# Create your models here.
class Notification(models.Model):
    # foreingKey con dataSystem
    #dataSystem = models.ForeignKey("notification.dataSystem", on_delete=models.CASCADE)# Se evita tener que usar jeraquía al crear clases
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    body = models.TextField()
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title