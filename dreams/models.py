from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Dream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dream_audio = models.FileField(upload_to='../static/audio')
    dream_text = models.CharField(max_length=100000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('dream_update', kwargs={'pk': self.pk})
