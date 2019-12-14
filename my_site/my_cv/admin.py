from django.contrib import admin
from . import models


class ExperienceOrOutreachAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'current_position', 'is_outreach',)
    date_hierarchy = 'start_date'


admin.site.register(models.Resume)
admin.site.register(models.PersonalLink)
admin.site.register(models.University)
admin.site.register(models.ExperienceOrOutreach, ExperienceOrOutreachAdmin)
