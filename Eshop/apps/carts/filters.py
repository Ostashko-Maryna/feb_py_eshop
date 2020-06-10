from django_filters.rest_framework import FilterSet
from django_filters import DateRangeFilter, DateFilter


class CartFilter(FilterSet):
    
    start_date = DateFilter(field_name='created_on', 
                            lookup_expr=('gt'), 
                            label='Створено після'
                            ) 
    end_date = DateFilter(field_name='created_on',
                          lookup_expr=('lt'),
                            label='Створено до'
                          )
    date_range = DateRangeFilter(field_name='created_on')


class CartItemFilter(FilterSet):

    start_date = DateFilter(field_name='created_on', 
                            lookup_expr=('gt'), 
                            label='Створено після'
                            ) 
    end_date = DateFilter(field_name='created_on',
                          lookup_expr=('lt'),
                            label='Створено до'
                          )
    date_range = DateRangeFilter(field_name='created_on')    

  
    

