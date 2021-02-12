from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
  name = forms.CharField(label='Name')
  email = forms.EmailField(label='Email')
  subject = forms.CharField(label='Subject')
  message = forms.CharField(label='Message', widget=forms.Textarea())

  def send_mail(self):
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    subject = self.cleaned_data['subject']
    message = self.cleaned_data['message']

    content = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMensagem: {message}'

    mail = EmailMessage(
      subject='Email from django2 system',
      body=content,
      from_email='contact@email.com',
      to=['receiver@email.com'],
      headers={'Reply-To': email},
    )

    mail.send()

