from django import forms
import re
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tên tài khoản', max_length=50)
    last_name = forms.CharField(label='Số điện thoại', max_length=19)
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không trùng nhau rồi...")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặt biệt hoặc dấu cách rồi...")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tên tài khoản đã tồn tại rồi...")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], last_name=self.cleaned_data['last_name'], password=self.cleaned_data['password1'])
