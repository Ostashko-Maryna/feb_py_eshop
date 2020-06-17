from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Stats
from .serializers import StatsSerializer
from .filters import StatsFilter


class StatsList(generics.ListCreateAPIView):
    serializer_class = StatsSerializer
    pagination_class = LimitOffsetPagination
    filter_class = StatsFilter

    def get_queryset(self):
        if 'search' in self.request.query_params:
            search_name = self.request.query_params['search']
            return Stats.objects.filter(name__icontains=search_name)
        return Stats.objects.all()


class StatsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatsSerializer

    def get_object(self):
        obj = get_object_or_404(Stats, pk=self.kwargs.get('statss_id'))
        return obj
