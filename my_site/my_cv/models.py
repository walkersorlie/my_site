from django.db import models
from django.utils import timezone


class Resume(models.Model):
    resume_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    personal_links = models.ManyToManyField('PersonalLink', blank=True)
    education = models.ManyToManyField('Education', blank=True)
    experience = models.ManyToManyField('ExperienceOrOutreach', blank=True)
    skills = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    is_current_resume = models.BooleanField(default=False)
    date_created = models.DateTimeField()
    last_edited = models.DateTimeField()


    class Meta:
        ordering = ['-is_current_resume']
        verbose_name_plural = "Resumes"

    def __str__(self):
        return self.resume_name.title()

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
            self.last_edited = timezone.now()
        else:
            self.last_edited = timezone.now()

        super(Resume, self).save(*args, **kwargs)


class PersonalLink(models.Model):
    site_name = models.CharField(max_length=60)
    url = models.URLField()


    class Meta:
        ordering = ['site_name']

    def __str__(self):
        return self.site_name


class Education(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    url = models.URLField()
    slug = models.SlugField(max_length=200, blank=True)


    class Meta:
        ordering = ['name']
        verbose_name_plural = "Education"

    def get_absolute_url(self):
        return reverse('my_cv:education_detail_view', args=[self.slug, self.id])

    def __str__(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Education, self).save(*args, **kwargs)


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
    slug = models.SlugField(max_length=200, blank=True)


    class Meta:
        ordering = ['opportunity_name']
        verbose_name = "Experience/Outreach"
        verbose_name_plural = "Experience/Outreach"

    def get_absolute_url(self):
        return reverse('my_cv:experience_outreach_detail_view', args=[self.slug, self.id])

    def __str__(self):
        return self.opportunity_name.title()

    def save(self, *args, **kwargs):
        """
        Do something with 'current_position' to not show 'end_date'?? Not sure what I want yet
        """
        self.slug = slugify(self.opportunity_name)

        super(ExperienceOrOutreach, self).save(*args, **kwargs)
