from django.contrib import admin
from .models import Journal, Submission, Tag

admin.site.register(Journal)
admin.site.register(Submission)
admin.site.register(Tag)