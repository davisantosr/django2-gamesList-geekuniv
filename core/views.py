from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Product
from .forms import ContactForm, ProductModelForm



def index(request):
  context = {
    'products': Product.objects.all()
  }
  return render(request, 'index.html', context)


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
  if str(request.user) != 'AnonymousUser':
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
  else:
    return redirect('index')

