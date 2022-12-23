from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *
class AddPlaceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['people'].empty_label = 'не выбрано'       #изменяем конструктор чтобы опр текст в выборе
    class Meta:
        model = Place
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),     #задаем визул каждого поля из модели
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_name(self):                               #персональная валидация атрибута из модели
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длинна превышает 200 сиволов')
        return name

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
