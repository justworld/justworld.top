import json

from django.forms import ValidationError, models

from .models import Article


class ArticleForm(models.ModelForm):
    def clean_tags(self):
        tags = self.data.getlist('tags')
        return tags