from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required': u'please input username.'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required': u'please input password.'})

    def clean(self):
        super(LoginForm, self).clean()
        username = self.cleaned_data.get('username', '').strip()
        password = self.cleaned_data.get('password', '').strip()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                self._errors['username'] = self.error_class([u'Oh, fuck!  username or password error.'])
                del self.cleaned_data['username']
                del self.cleaned_data['password']
        return self.cleaned_data
