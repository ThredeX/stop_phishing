from urllib.parse import urlparse
from django import forms
from django.core import validators
from . import models

# TODO: fix validation always fail


class PhishingUrlForm(forms.ModelForm):

    class Meta:
        model = models.PhishingUrl
        fields = ('domain',)

    def clean_domain(self):
        validator = validators.URLValidator()
        validator(self.cleaned_data['domain'])

        self.cleaned_data['domain'] = urlparse(
            self.cleaned_data['domain']).netloc
