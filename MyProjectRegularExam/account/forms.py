from django import forms
from MyProjectRegularExam.account.models import Profile

class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        max_length=Profile.MAX_PASSWORD_LENGTH,
    )

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


