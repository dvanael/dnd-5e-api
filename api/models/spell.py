from django.db import models
from .magic_school import MagicSchool
from .damage_type import DamageType
from .ability_score import AbilityScore


class Spell(models.Model):
    index = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    desc = models.JSONField()
    higher_level = models.JSONField(null=True, blank=True)
    range = models.CharField(max_length=100)
    components = models.JSONField()
    material = models.CharField(max_length=100, null=True, blank=True)
    ritual = models.BooleanField()
    duration = models.CharField(max_length=100)
    concentration = models.BooleanField()
    casting_time = models.CharField(max_length=100)
    level = models.IntegerField()
    school = models.ForeignKey(
        MagicSchool, on_delete=models.CASCADE, related_name="spells"
    )
    area_of_effect = models.JSONField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    # Heal
    heal_at_slot_level = models.JSONField(null=True, blank=True)

    # Damage
    damage_type = models.ForeignKey(
        DamageType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="spells",
    )
    damage_at_slot_level = models.JSONField(null=True, blank=True)

    # DC
    dc_type = models.ForeignKey(
        AbilityScore,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="spells",
    )
    dc_success = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Spell"
        verbose_name_plural = "Spells"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.index = self.name.lower().replace(" ", "-")
        self.url = f"/api/spells/{self.index}"
        return super().save(*args, **kwargs)
