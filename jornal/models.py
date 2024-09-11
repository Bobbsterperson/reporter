from django.db import models

class Journal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Submission(models.Model):
    text = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(
        Journal, on_delete=models.CASCADE,
        related_name='submissions',
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='submissions', blank=True)

    def __str__(self):
        return self.text
