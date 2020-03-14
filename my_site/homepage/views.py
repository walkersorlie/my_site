from django.views import generic
from my_cv.models import Education, ExperienceOrOutreach
from .models import HomepageBlurb


class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'blurb'

    def get_queryset(self):
        return HomepageBlurb.objects.last()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['education'] = Education.objects.all()
        context['experience'] = ExperienceOrOutreach.objects.all()

        # context['both'] = {
        #     'education': Education.objects.all(),
        #     'experience': ExperienceOrOutreach.objects.all()
        #     }

        both_list = []
        better_both_list = []
        for school in Education.objects.all():
            both_list.append((school, 'education'))
            better_both_list.append((school, 'education'))

        for experience in ExperienceOrOutreach.objects.all():
            if experience.current_position or experience.is_outreach:
                better_both_list.append((experience, 'experience'))
            both_list.append((experience, 'experience'))

        context['both'] = both_list
        context['edu_exp_list'] = better_both_list

        return context
