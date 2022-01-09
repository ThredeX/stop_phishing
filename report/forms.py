from urllib.parse import urlparse
from django import forms
from django.core import validators
from . import models

from django.utils.translation import gettext_lazy as _


class PhishingUrlForm(forms.ModelForm):

    class Meta:
        model = models.PhishingUrl
        fields = ('domain',)
        widgets = {'domain': forms.URLInput(
            attrs={'placeholder': 'https://phishing.thredex.eu/'})}
        error_messages = {
            'domain': {
                'required': _('You need to provide a URL'),
                'unique': _('This URL is already in our database!')
            },
        }

    def clean_domain(self):
        validator = validators.URLValidator()
        validator(self.cleaned_data['domain'])
        parsed_domain = urlparse(
            self.cleaned_data['domain']).netloc
        return parsed_domain
