from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm, ProductModelForm


def index(request):
  return render(request, 'index.html')


def contact(request):
  form = ContactForm(request.POST or None)

  if str(request.method) == 'POST':
    if form.is_valid():
      form.send_mail()
  
      messages.success(request, 'Email sent successfully')
      form = ContactForm()

    else:
      messages.error(request, 'Error when tried to sent the email')

  else:
    context = {
      'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
  if str(request.method) == 'POST':
    form = ProductModelForm(request.POST, request.FILES)

    if form.is_valid():
      prod = form.save(commit=False)

      form.save()
      
      messages.success(request, 'Product saved.')
      form = ProductModelForm()
    else:
      messages.error(request, 'Error when tried to save')
  else:
    form = ProductModelForm()
  contexta = {
    'form': form
  }
  return render(request, 'product.html', contexta)

