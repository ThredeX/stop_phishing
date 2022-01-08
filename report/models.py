from django.db import models


class PhishingUrl(models.Model):
    domain = models.CharField('phising url', primary_key=True, max_length=64)
    is_verified = models.BooleanField('is really phishing', default=False)

    def __str__(self):
        return self.domain
