from django import forms
from AppTwo.models import UserInfo

class Formpage(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class Usersignup(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
