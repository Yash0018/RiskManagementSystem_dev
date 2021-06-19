from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from .models import *
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import *
from .serializers import *
from django_elasticsearch_dsl_drf.filter_backends import (FilteringFilterBackend, OrderingFilterBackend, CompoundSearchFilterBackend)


def generate_random_data():
    url = 'https://newsapi.org/v2/everything?q=apple&from=2021-04-23&to=2021-04-23&sortBy=popularity&apiKey=b563875892b741e6a7f18708c985bd73'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    for data in payload.get('articles'):
        print(count)
        ElasticDemo.objects.create(
            title=data.get('title'),
            content=data.get('description')
        )


def index(request):
    generate_random_data()
    return JsonResponse({'status': 200})


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend
    ]

    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
        'title',
        'content',
    )
    filter_fields = {
        'title': 'title',
        'content': 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ('id',)