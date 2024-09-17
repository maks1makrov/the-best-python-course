import os

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from all.forms import EnrollmentForm
from all.models import Enrollment

import logging

from src.settings import BASE_DIR

logger = logging.getLogger(__name__)


# @method_decorator(cache_page(5), name='dispatch')
class AllMain(View):

    def get(self, request):
        try:
            context = {'form': EnrollmentForm()}
            # int('af')
            # return render(request, 'Copy_of_Max.html', context)
            # logger.error(f"os.path.join(BASE_DIR, 'templates_not_used') - {os.path.join(BASE_DIR, 'templates_not_used')}")
            # print(os.path.join(BASE_DIR, 'templates') )
            return render(request, 'index_vital.html', context)
        except Exception as ex:
            logger.error(f'{ex.__str__()}')
            return redirect('enroll_error')

class AllMainOld(View):

    def get(self, request):
        try:
            context = {'form': EnrollmentForm()}
            # int('af')
            # return render(request, 'Copy_of_Max.html', context)
            # logger.error(f"os.path.join(BASE_DIR, 'templates_not_used') - {os.path.join(BASE_DIR, 'templates_not_used')}")
            # print(os.path.join(BASE_DIR, 'templates') )
            return render(request, 'index_g5.html', context)
        except Exception as ex:
            logger.error(f'{ex.__str__()}')
            return redirect('enroll_error')
class EnrollmentView(View):
    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_full = request.POST.get('phone_full')
            course = request.POST.get('course')
            message = request.POST.get('message', '')

            # Проверяем, что хотя бы одно из полей (email, phone или message) заполнено
            if not (email or phone_full or message):
                return redirect('enroll_error')

            enrollment = Enrollment(
                name=name,
                email=email,
                phone=phone_full,
                course=course,
                message=message
            )
            enrollment.save()
        except Exception as ex:
            logger.error(f'{ex.__str__()}')
            return redirect('enroll_error')
        return redirect('enroll_success')


def enroll_success(request):
    return render(request, 'enroll_success.html')


def enroll_error(request):
    return render(request, 'enroll_error.html')