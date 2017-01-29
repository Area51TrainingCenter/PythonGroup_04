from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        password1_ = self.cleaned_data.get('password1')
        password2_ = self.cleaned_data.get('password2')

        if password1_ != password2_:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return self.cleaned_data

    def save(self, commit=True):
        instancia = super(RegistroForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        instancia.set_password(password)
        if commit:
            instancia.save()
        return instancia

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        usuario_ = self.cleaned_data.get('usuario')
        password_ = self.cleaned_data.get('password')

        usuario_auth = authenticate(username=usuario_, password=password_)
        if not usuario_auth:
            raise forms.ValidationError('Usuario/password no existen')
        else:
            self.cleaned_data['usuario'] = usuario_auth
        return self.cleaned_data
