from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Enrollment(models.Model):
    COURSE_CHOICES = [
        ('basic_python', 'Основы Python'),
        ('advanced_python', 'Продвинутый курс по Python'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    message = models.TextField(blank=True, null=True)  # Другой способ связи, пожелания, предложения
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.course}'
