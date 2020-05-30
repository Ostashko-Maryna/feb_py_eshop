import django_filters
from .models import Payments, paymentsystem_list

class PaymentsFilter(django_filters.FilterSet):
    user = django_filters.filters.CharFilter(lookup_expr='icontains')
    id = django_filters.NumberFilter()
    billAmount = django_filters.NumberFilter()
    paymentsystem = django_filters.filters.ChoiceFilter(
        choices=paymentsystem_list
    )
    # paymentdate = django_filters.DateTimeFilter(
        # 'start', lookup_expr='contains'
    # )

    class Meta:
        model = Payments
        fields = [
            'id', 
            'user', 
            'billAmount',
            'paymentsystem',
            # 'paymentdate',
        ]
