from urllib.parse import urlparse
from django import forms
from django.core import validators
from . import models


class PhishingUrlForm(forms.ModelForm):

    class Meta:
        model = models.PhishingUrl
        fields = ('domain',)

    def clean_domain(self):
        validator = validators.URLValidator()
        validator(self.cleaned_data['domain'])

        parsed_domain = urlparse(
            self.cleaned_data['domain']).netloc
        return parsed_domain
