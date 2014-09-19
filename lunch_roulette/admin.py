from django.contrib import admin

from . import models
# Register your models here.
class LunchGroupAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.LunchGroup, LunchGroupAdmin)


class ParticipantAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Participant, ParticipantAdmin)
