from django.contrib import admin
from . import models


class ResumeAdmin(admin.ModelAdmin):
    exclude = ('date_created', 'last_edited')
    list_display = ('__str__', 'resume_file', 'is_current_resume', 'date_created', 'last_edited')
    list_filter = ('education__name', 'experience__opportunity_name', 'is_current_resume')
    search_fields = ('resume_name',)

    def resume_file(self, obj):
        return obj.resume
    resume_file.short_description = 'File Name'


class ExperienceOrOutreachAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    list_display = ('__str__', 'current_position', 'is_outreach',)


admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.PersonalLink)
admin.site.register(models.Education)
admin.site.register(models.ExperienceOrOutreach, ExperienceOrOutreachAdmin)
