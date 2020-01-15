from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
        path('home',TemplateView.as_view(template_name='home.html'),name='login'),
        path('student-attendence',TemplateView.as_view(template_name='student-attendence.html'),name='student-attendence'),
        path('student-assessment',TemplateView.as_view(template_name='student-assessment.html'),name='student-assessment'),
        path('student-leave-management',TemplateView.as_view(template_name='student-leave-management.html'),name='student-leave-management'),
        path('student-applied-leave',TemplateView.as_view(template_name='student-applied-leave.html'),name='student-applied-leave'),
        path('notification',TemplateView.as_view(template_name='notification.html'),name='notification'),
        path('student-profile',TemplateView.as_view(template_name='student-profile.html'),name='student-profile'),
        path('announcement',TemplateView.as_view(template_name='announcement.html'),name='announcement'),
        path('log',TemplateView.as_view(template_name='login.html'),name='log'),

        path('student_leave',views.student_leave,name='student_leave'),
        
       
        
]