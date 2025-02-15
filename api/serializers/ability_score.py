from rest_framework import serializers
from ..models.ability_score import AbilityScore


class AbilityScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbilityScore
        fields = ["index", "name", "full_name", "desc", "url", "updated_at"]


class AbilityScoreSpellSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbilityScore
        fields = ["index", "name", "url"]
