from django import forms
from .models import Voter
from django.contrib.auth.forms import UserCreationForm

class EditForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = "__all__"

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = "__all__"

# class VoterForm(forms.ModelForm):
#     class Meta:
#         model = Voter
#         fields = ("v_id", "name", "a_id", "age", "dob","sex","phone_no","email","city","state")

#         widgets = {
#             "v_id" : forms.NumberInput(attrs={'class': 'ui field', 'placeholder': 'Voter ID'}),
#             "name" : forms.TextInput(attrs={'class': 'ui field', 'placeholder': 'Name'}),
#             "a_id" : forms.NumberInput(attrs={'class': 'ui field', 'placeholder': 'Aadhar ID'}),
#             "age" : forms.NumberInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#             "dob" : forms.DateInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#             "age" : forms.NumberInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#             "sex" : forms.TextInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#             "phone_no" : forms.TextInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#             "email" : forms.EmailInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#             "city" : forms.TextInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#             "state" : forms.TextInput(attrs={'class': 'ui field', 'placeholder': 'Age'}),
#         }         