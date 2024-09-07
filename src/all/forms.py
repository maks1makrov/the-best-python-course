from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    # phone = PhoneNumberField(
    #     widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control', 'id': 'phone', 'required': True}),
    #     label='Телефон'
    # )
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('Phone')}),

                       label=("Phone number"), required=False)

    class Meta:
        model = Enrollment
        fields = ['name', 'email', 'phone', 'course', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'required': True}),
            'course': forms.Select(attrs={'class': 'form-control', 'id': 'course', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'rows': 4}),
        }
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'course': 'Курс',
            'message': 'Сообщение',
        }