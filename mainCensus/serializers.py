from rest_framework import serializers
from .models import General,Homes, Homested

class GeneralSerializers(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ('hs_code', 'hm_code', 'name', 'relationshipToHead', 'sex')


class HomesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homes
        fields = ('hm_code', '')


class HomestedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homested
        fields = ('hs_code', '')