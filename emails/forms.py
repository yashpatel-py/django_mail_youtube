from django import forms

class ContactUsForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(), required=True)
    last_name = forms.CharField(widget=forms.TextInput(), required=True)
    email_id = forms.EmailField(widget=forms.TextInput(), required=True)
    phone_number = forms.CharField(widget=forms.TextInput(), required=True)
    subject = forms.CharField(widget=forms.TextInput(), required=True)
    message = forms.CharField(widget=forms.TextInput(), required=True)