from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.models import ModelMultipleChoiceField


class FilteredMultiSelectField(models.CharField):
    """
    过滤多选字段
    """

    def get_db_prep_save(self, value, connection):
        value = super(FilteredMultiSelectField, self).get_db_prep_save(value, connection)
        if isinstance(value, set):
            value = list(value)
        if value:
            return ','.join(str(x) for x in value)
        return ''

    def from_db_value(self, value, expression, connection, context):
        if value:
            return value.split(',')
        return []

    def to_python(self, value):
        if isinstance(value, list):
            return value
        return []

    def formfield(self, **kwargs):
        defaults = {'required': not self.blank,
                    'label': self.verbose_name,
                    'help_text': self.help_text,
                    'widget': FilteredSelectMultiple(self.verbose_name, False)}
        defaults.update(kwargs)
        return ModelMultipleChoiceField(**defaults)
