from django import forms
from app1.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'contact', 'course', 'fee','address']