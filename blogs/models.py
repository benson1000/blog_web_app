from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
