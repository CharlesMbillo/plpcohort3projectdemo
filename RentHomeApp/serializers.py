from .models import RentHome
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class homeserilizer(GeoFeatureModelSerializer):
    class Meta:
        model = RentHome
        geo_field='location'
        fields =('rent_capacity','rent')