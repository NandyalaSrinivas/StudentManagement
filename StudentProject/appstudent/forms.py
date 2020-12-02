from django.forms import ModelForm
from appstudent.models import Application, Register


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['email', 'fullname', 'marks_ssc', 'marks_inter']


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
