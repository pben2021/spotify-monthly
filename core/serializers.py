from rest_framework import serializers
from .models import Year , January, February, March, April, May, June, July, August, September, October, November, December

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ('id', 'month', 'url')

class JanuarySerializer(serializers.ModelSerializer):
    class Meta:
        model = January
        fields = ('id', 'title', 'artist', 'url', 'place')

class FebruarySerializer(serializers.ModelSerializer):
    class Meta:
        model = February
        fields = ('id', 'title', 'artist', 'url', 'place')

class MarchSerializer(serializers.ModelSerializer):
    class Meta:
        model = March
        fields = ('id', 'title', 'artist', 'url', 'place')

class AprilSerializer(serializers.ModelSerializer):
    class Meta:
        model = April
        fields = ('id', 'title', 'artist', 'url', 'place')

class MaySerializer(serializers.ModelSerializer):
    class Meta:
        model = May
        fields = ('id', 'title', 'artist', 'url', 'place')

class JuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = June
        fields = ('id', 'title', 'artist', 'url', 'place')

class JulySerializer(serializers.ModelSerializer):
    class Meta:
        model = July
        fields = ('id', 'title', 'artist', 'url', 'place')

class AugustSerializer(serializers.ModelSerializer):
    class Meta:
        model = August
        fields = ('id', 'title', 'artist', 'url', 'place')

class SeptemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = September
        fields = ('id', 'title', 'artist', 'url', 'place')

class OctoberSerializer(serializers.ModelSerializer):
    class Meta:
        model = October
        fields = ('id', 'title', 'artist', 'url', 'place')

class NovemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = November
        fields = ('id', 'title', 'artist', 'url', 'place')

class DecemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = December
        fields = ('id', 'title', 'artist', 'url', 'place')

