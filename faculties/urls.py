from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
        path('',TemplateView.as_view(template_name='index.html'),name='index'),
        path('faculty_login',TemplateView.as_view(template_name='faculty-login.html'),name='faculty-login'),
        path('faculty_home_batch',TemplateView.as_view(template_name='faculty_home_batch.html'),name='faculty-home_batch'),
        path('faculty_student_leave',TemplateView.as_view(template_name='faculty_student_leave.html'),name='faculty_student_leave'),
        path('login',TemplateView.as_view(template_name='login.html'),name='login'),
        path('faculty_profile_edit',TemplateView.as_view(template_name='faculty_profile_edit.html'),name='faculty_profile_edit'),
        path('faculty-profile',TemplateView.as_view(template_name='faculty-profile.html'),name='faculty-profile'),
        path('student-leave',TemplateView.as_view(template_name='student-leave.html'),name='student-leave'),
        path('assessment',TemplateView.as_view(template_name='assessment.html'),name='assessment'),
        path('attendence_1',TemplateView.as_view(template_name='attendence_1.html'),name='attendence_1'),
        path('leave-forwarded',TemplateView.as_view(template_name='leave-forwarded.html'),name='leave-forwarded'),
        path('leave-rejected',TemplateView.as_view(template_name='leave-rejected.html'),name='leave-rejected'),
        path('notifications',TemplateView.as_view(template_name='notifications.html'),name='notifications'),
        path('home',TemplateView.as_view(template_name='home.html'),name='home'),

        path('fac-login',views.signin,name='logins'),
        path('fassessment',views.fassessment,name='fassessment'),


        
]