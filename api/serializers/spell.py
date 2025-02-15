from rest_framework import serializers
from ..models.spell import Spell, MagicSchool


class MagicSchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagicSchool
        fields = ["index", "name", "url"]


class SpellSerializer(serializers.ModelSerializer):
    school = MagicSchoolSerializer()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {key: value for key, value in data.items() if value is not None}

    class Meta:
        model = Spell
        fields = [
            "index",
            "name",
            "desc",
            "higher_level",
            "range",
            "components",
            "ritual",
            "duration",
            "concentration",
            "casting_time",
            "level",
            "school",
            "heal_at_slot_level",
            "damage",
            "dc",
            "area_of_effect",
            "url",
            "updated_at",
        ]
