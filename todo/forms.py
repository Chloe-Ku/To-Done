"""
This module defines forms for the todo app.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateItemTextForm(forms.Form):
    """This class updates the ItemTextForm"""
    item_text = forms.Textarea()
    # hidden_item_id = forms.CharField(label=)

class NewUserForm(UserCreationForm):
    """This class handles the NewUserForm"""
    email = forms.EmailField(required=True)

    class Meta:
        """This class handles the meta fields"""
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        """This method saves the form"""
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
