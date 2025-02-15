from django.db import models


class MagicSchool(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Magic School"
        verbose_name_plural = "Magic Schools"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        url = f"/api/magic-schools/{self.index}"
        self.url = url
        return super().save(*args, **kwargs)


class Spell(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    desc = models.JSONField()
    higher_level = models.JSONField()
    range = models.CharField(max_length=100)
    components = models.JSONField()
    ritual = models.BooleanField()
    duration = models.CharField(max_length=100)
    concentration = models.BooleanField()
    casting_time = models.CharField(max_length=100)
    level = models.IntegerField()
    school = models.ForeignKey(
        MagicSchool, on_delete=models.CASCADE, related_name="spells"
    )
    url = models.CharField(max_length=100, null=True, blank=True)

    heal_at_slot_level = models.JSONField(null=True, blank=True)
    damage = models.JSONField(null=True, blank=True)
    dc = models.JSONField(null=True, blank=True)
    area_of_effect = models.JSONField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Spell"
        verbose_name_plural = "Spells"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        url = f"/api/spells/{self.index}"
        self.url = url
        return super().save(*args, **kwargs)
