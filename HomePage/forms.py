from django import forms
# from django.contrib.auth import login

from HomePage.models import UserRegister


class registerForm(forms.ModelForm):
    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if UserRegister.objects.filter(user_name=user).exists():
            raise forms.ValidationError('user exist')
        return user
    def clean_email(self):
        email=self.cleaned_data['email']
        if UserRegister.objects.filter(email=email).exists():
            raise forms.ValidationError('email exist')
        return email

    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1!=password2:
            raise forms.ValidationError('password not match')
        elif len(password2)<8:
            raise forms.ValidationError('password is too short')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('upper letter use please')
        return password2
    class Meta:
        model = UserRegister
        fields = ['user_name', 'email', 'first_name' , 'last_name','password1','password2']


# #----------------------------------------------------login:
#
class UserLoginForm(forms.Form):
    user=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please enter username'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please enter password'}))






