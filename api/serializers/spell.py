from rest_framework import serializers
from .magic_school import MagicSchoolSpellSerializer
from .damage_type import DamageTypeSpellSerializer
from .ability_score import AbilityScoreSpellSerializer
from ..models.spell import Spell


class SpellSerializer(serializers.ModelSerializer):
    school = MagicSchoolSpellSerializer()
    damage = serializers.SerializerMethodField()
    dc = serializers.SerializerMethodField()

    def get_damage(self, instance):
        if instance.damage_type and instance.damage_at_slot_level:
            return {
                "type": DamageTypeSpellSerializer(instance.damage_type).data,
                "damage_at_slot_level": instance.damage_at_slot_level,
            }

    def get_dc(self, instance):
        if instance.dc_type and instance.dc_success:
            return {
                "dc_type": AbilityScoreSpellSerializer(instance.dc_type).data,
                "dc_scuccess": instance.dc_success,
            }

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
            "material",
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
