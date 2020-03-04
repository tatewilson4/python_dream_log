from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Dream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    dream_audio = models.FileField(upload_to='dreams/', blank=True)
    dream_text = models.CharField(max_length=100000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dream_update', kwargs={'pk': self.pk})
