from django import forms
from sendemail.tasks import send_emails_tasks

class ContactFormEmail(forms.Form):
    email = forms.CharField(required=True, widget=forms.Textarea)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def send_email(self):
        print(self.cleaned_data['email'])
        print(self.cleaned_data['subject'])
        print(self.cleaned_data['message'])
        users = self.cleaned_data['email'].split(",")
        print(users)
        for user in users:
            to_email = user
            print(to_email)
        send_emails_tasks.delay(
            self.cleaned_data['email'], self.cleaned_data['subject'], self.cleaned_data['message'],
        )