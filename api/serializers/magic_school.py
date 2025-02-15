from rest_framework import serializers
from ..models.spell import MagicSchool


class MagicSchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagicSchool
        fields = ["index", "name", "desc", "url", "updated_at"]


class MagicSchoolSpellSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagicSchool
        fields = ["index", "name", "url"]
