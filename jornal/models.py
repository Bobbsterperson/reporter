from django.db import models

class Submission(models.Model):
    text = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
