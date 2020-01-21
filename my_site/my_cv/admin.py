from django.contrib import admin
from . import models


class ResumeAdmin(admin.ModelAdmin):
    exclude = ('date_created', 'last_edited', 'slug')
    list_display = ('__str__', 'resume_file', 'is_current_resume', 'date_created', 'last_edited')
    list_filter = ('education__name', 'experience__name', 'is_current_resume')
    search_fields = ('resume_name',)

    def resume_file(self, obj):
        return obj.resume
    resume_file.short_description = 'File Name'


class EducationAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class ExperienceOrOutreachAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    exclude = ('slug',)
    list_display = ('__str__', 'current_position', 'is_outreach',)


admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.PersonalLink)
admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.ExperienceOrOutreach, ExperienceOrOutreachAdmin)
