from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, seriesComment
from captcha.fields import CaptchaField
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput,
                                help_text='Enter the same password again for verification!')
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1
    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('The entered passwords do not match', code='password_mismatch')}
            raise ValidationError(errors)
    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'Movie': forms.HiddenInput}
class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Write text in picture', error_messages={'invalid': 'Wrong text'})

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'Movie': forms.HiddenInput}

class SeriesUserCommentForm(forms.ModelForm):
    class Meta:
        model = seriesComment
        exclude = ('is_active',)
        widgets = {'Series': forms.HiddenInput}
class SeriesGuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Write text in picture', error_messages={'invalid': 'Wrong text'})

    class Meta:
        model = seriesComment
        exclude = ('is_active',)
        widgets = {'Series': forms.HiddenInput}
