from http import HTTPStatus

from rest_framework import filters, mixins, viewsets
from rest_framework.response import Response

from .exceptions import PriceError, DepositError, TermError
from .serializers import OfferSerializer
from offer.models import Offer


def calculate_payment(queryset, *args):
    """ Calculate minimal payment with given conditions. """

    price, deposit, term = args
    for note in queryset:
        note.payment = (
            (price - deposit*note.rate_min/12)
            / (1 - (1 + note.rate_min/12) * (1 - term*12))
        )
        note.save()


def check_values(price, deposit, term):
    """ Checking values of price, deposit and term. """

    if price is not None and int(price) < 0:
        raise PriceError()
    if deposit is not None and int(deposit) < 0:
        raise DepositError()
    if term is not None and int(term) < 0:
        raise TermError()



class CreateDeletePatchViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """ Viewset to define requests. """

    pass


class OfferViewSet(CreateDeletePatchViewSet):
    """ Vieset for Offer model. """

    serializer_class = OfferSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = (
        'rate_min', 'rate_max', 'payment_min', 'payment_max', 'payment',
    )

    def get_queryset(self):
        queryset = Offer.objects.all()
        price = self.request.query_params.get('price', None)
        deposit = self.request.query_params.get('deposit', None)
        term = self.request.query_params.get('term', None)
        check_values(price, deposit, term)
        if None not in (price, deposit, term):
            price, deposit, term = map(int, (price, deposit, term))
            queryset = Offer.objects.filter(
                term_min__lte=term,
                term_max__gte=term,
                payment_min__lte=(price-deposit),
                payment_max__gte=(price-deposit),
            )
            calculate_payment(queryset, price, deposit, term)
        return queryset
