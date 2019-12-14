from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/resume/<filename>
    return 'user_{0}/resume/{1}'.format(instance.user.id, filename)


class Resume(models.Model):
    location = models.CharField(max_length=50)
    email = models.EmailField()
    personal_links = models.ForeignKey('PersonalLink', on_delete=models.CASCADE)
    education = models.ForeignKey('University', on_delete=models.CASCADE)
    experience = models.ForeignKey('ExperienceOrOutreach', on_delete=models.CASCADE)
    skills = models.TextField()
    interests = models.TextField()
    resume = models.FileField(upload_to=user_directory_path)


    class Meta:
        verbose_name_plural = "Resumes"


    def __str__(self):
        return "Resume"


class PersonalLink(models.Model):
    site_name = models.CharField(max_length=60)
    url = models.URLField()


    def __str__(self):
        return self.site_name


class University(models.Model):
    university_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    duration = models.DurationField()
    description = models.TextField()
    university_url = models.URLField()


    class Meta:
        verbose_name_plural = "Universities"


    def __str__(self):
        return self.university_name.title()


class ExperienceOrOutreach(models.Model):
    opportunity_name = models.CharField(max_length=200)
    position_title = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    current_position = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_outreach = models.BooleanField()
    opportunity_url = models.URLField(blank=True)


    class Meta:
        verbose_name = "Experience/Outreach"
        verbose_name_plural = "Experience/Outreach"


    def __str__(self):
        return self.opportunity_name.title()

    def save(self, *args, **kwargs):
        """
        Do something with 'current_position' to not show 'end_date'?? Not sure what I want yet
        """

        super().save(*args, **kwargs)
