from django.urls import path
from . import views

app_name = 'my_cv'
urlpatterns = [

    # /my_cv/
    path('', views.IndexView.as_view(), name = 'index'),

    # /my_cv/resumes/
    path('resumes/', views.ResumeIndexView.as_view(), name = 'resume_index'),
    # /my_cv/resumes/<slug>_<pk>/
    path('resumes/<slug>_<pk>/', views.ResumeDetailView.as_view(), name = 'resume_detail_view'),

    # /my_cv/education/
    path('education/', views.EducationIndexView.as_view(), name = 'education_index'),
    # /my_cv/education/<slug>_<pk>/
    path('education/<slug>_<pk>/', views.EducationDetailView.as_view(), name = 'education_detail_view'),

    # /my_cv/experience_outreach/
    path('experience_outreach/', views.ExperienceOrOutreachIndexView.as_view(), name = 'experience_outreach_index'),
    # /my_cv/experience_outreach/<slug>_<pk>/
    path('experience_outreach/<slug>_<pk>/', views.ExperienceOrOutreachDetailView.as_view(), name = 'experience_outreach_detail_view'),

]
