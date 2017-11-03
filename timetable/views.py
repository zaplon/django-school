# -*- coding: utf-8 -*-
from timetable.models import Card
from rest_framework import serializers, viewsets


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_fields = ('students', 'teachers')

