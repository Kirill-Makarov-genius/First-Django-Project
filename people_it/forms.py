from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from people_it.models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    
    class Meta:
        model = PeopleIt
        fields = ("name", "who_is", "what_did","achievements", "photo", "cat")
        widgets = {
            'name': forms.TextInput(attrs={"class":"form_input"}),
            'what_did': forms.Textarea(attrs={"cols":60, "rows":20})
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 15:
            raise ValidationError("Длина превышает 15 символов")
        return name

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput({"class":"form-input"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput({"class":"form-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput({"class":"form-input"}))
    password2 = forms.CharField(label="Повтор Пароля", widget=forms.PasswordInput({"class":"form-input"}))
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
