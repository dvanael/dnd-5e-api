from django.contrib import admin
from .models import Spell, MagicSchool, DamageType, AbilityScore

# Register your models here.
admin.site.register(Spell)
admin.site.register(MagicSchool)
admin.site.register(DamageType)
admin.site.register(AbilityScore)
