from rest_framework import serializers
from ..models.damage_type import DamageType


class DamageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageType
        fields = ["index", "name", "desc", "url", "updated_at"]


class DamageTypeSpellSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageType
        fields = ["index", "name", "url"]
