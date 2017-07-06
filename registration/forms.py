from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)

    
    class Meta:
        model = User
