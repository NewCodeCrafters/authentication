from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'admission_no', 'phone', "date_of_birth", 'password')
        
