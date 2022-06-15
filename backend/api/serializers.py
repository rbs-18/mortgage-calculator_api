from email.headerregistry import Group
from rest_framework import serializers

from offer.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    """ Serializer for Offer model. """

    class Meta:
        fields = ('__all__')
        model = Offer
