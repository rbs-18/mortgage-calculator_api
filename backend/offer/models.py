from django.db import models


class Offer(models.Model):
    """ Model for offers. """

    bank_name = models.CharField(
        'Name of bank', max_length=100, unique=True,
    )
    payment = models.IntegerField(
        'Minimal payment per month', blank=True, null=True,
    )
    term_min = models.IntegerField('Minimal term')
    term_max = models.IntegerField('Maximal term')
    rate_min = models.FloatField('Minimal rate')
    rate_max = models.FloatField('Maximal rate')
    payment_min = models.IntegerField('Minimal sum of credit')
    payment_max = models.IntegerField('Maximal sum of credit')
