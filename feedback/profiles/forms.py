from django import forms


class ProfileForm(forms.Form):
    user_image = forms.ImageField(label="Profile Image", required=True)
