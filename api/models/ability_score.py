from django.db import models


class AbilityScore(models.Model):
    index = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    desc = models.JSONField()
    url = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ability Score"
        verbose_name_plural = "Ability Scores"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.index = self.name.lower().replace(" ", "-")
        self.url = f"/api/ability-scores/{self.index}"
        return super().save(*args, **kwargs)
