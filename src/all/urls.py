from django.contrib import admin
from django.urls import path

from all import views
from all.views import AllMain, EnrollmentView, AllMainOld

urlpatterns = [
    path('', AllMain.as_view(), name='list_view_new'),
    path('old-school/', AllMainOld.as_view(), name='list_view'),
    path('enroll/', EnrollmentView.as_view(), name='enroll'),
    path('enroll/success/', views.enroll_success, name='enroll_success'),
    path('enroll/error/', views.enroll_error, name='enroll_error'),

]
