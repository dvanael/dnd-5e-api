from django.db import models


class DamageType(models.Model):
    index = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    desc = models.JSONField()
    url = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Damage Type"
        verbose_name_plural = "Damage Types"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.index = self.name.lower().replace(" ", "-")
        self.url = f"/api/damage-types/{self.index}"
        return super().save(*args, **kwargs)
