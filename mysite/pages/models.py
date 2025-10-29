from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # ✅ new
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
