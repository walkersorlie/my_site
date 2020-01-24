from django.shortcuts import render
from django.http import Http404
from django.views import generic
from . import models
from repositories.models import Repository
from django.db.models import Q


class IndexView(generic.ListView):
    model = models.Resume
    template_name = 'my_cv/index.html'
    context_object_name = 'current_resumes'

    def get_queryset(self):
        return models.Resume.objects.filter(is_current_resume=True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # context['current_resume'] = self.get_queryset()[:1]
        context['current_resume'] = models.Resume.objects.get(is_current_resume=True)

        # print(models.Resume._meta.get_fields())
        # print(models.Resume._meta.get_fields()[0])
        '''
        for resume in models.Resume.objects.all():
            print('Name: %s' % resume.resume_name)
            if resume.education:
                for education in resume.education.all():
                    print(education.name)
        for education in models.Education.objects.all():
            for edu in education.resume_set.all():
                print(edu.resume_name)
        '''


        context['personal_links'] = models.PersonalLink.objects.all()

        repo_list = Repository.objects.all()[:3]
        for repo in repo_list:
            repo.repo_name = repo.repo_name.replace('-', ' ').replace('_', ' ').title()

        context['repo_list'] = repo_list

        return context


class ResumeIndexView(generic.ListView):
    model = models.Resume
    template_name = 'my_cv/resumes.html'
    context_object_name = 'all_resumes'


class ResumeDetailView(generic.DetailView):
    model = models.Resume
    template_name = 'my_cv/resume_detail_view.html'
    context_object_name = 'resume'
    query_pk_and_slug = True


class EducationIndexView(generic.ListView):
    model = models.Education
    template_name = 'my_cv/education.html'
    context_object_name = 'all_education'


class EducationDetailView(generic.DetailView):
    model = models.Education
    template_name = 'my_cv/education_detail_view.html'
    context_object_name = 'institution'
    query_pk_and_slug = True


'''
Only shows objects that are current_position or outreach in the template!!!
'''
class ExperienceOrOutreachIndexView(generic.ListView):
    model = models.ExperienceOrOutreach
    template_name = 'my_cv/experience_outreach_index.html'
    context_object_name = 'all_experience'


    def get_queryset(self):
        return models.ExperienceOrOutreach.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExperienceOrOutreachIndexView, self).get_context_data(**kwargs)

        context['outreach_or_current'] = self.get_queryset().filter(Q(current_position=True) | Q(is_outreach=True))

        return context


class ExperienceOrOutreachDetailView(generic.DetailView):
    model = models.ExperienceOrOutreach
    template_name = 'my_cv/education_outreach_detail_view.html'
    context_object_name = 'opportunity'
    query_pk_and_slug = True
