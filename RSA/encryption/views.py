from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import send_mail

def home(request):
    formtext = TextForm()
    if request.method == 'POST':
        formtext = TextForm(request.POST)
        if formtext.is_valid():
            formtext.save()
            return redirect('/success/')

    context = {'formtext': formtext,
               }

    return render(request, 'encryption/home.html', context=context)


def success(request):

    openkey = Data_encryption.objects.all().order_by('-pk').values_list('open_key')[0][0]
    secretkey = Data_encryption.objects.all().order_by('-pk').values_list('secret_key')[0][0]
    encryptiontext = Data_encryption.objects.all().order_by('-pk').values_list('encrypted_text')[0][0]
    email = Data_encryption.objects.all().order_by('-pk').values_list('email')[0][0]
    usertext = Data_encryption.objects.all().order_by('-pk').values_list('user_text')[0][0]

    subject = 'Hello! Here is your keys from RSA-encryption.com.'
    message = 'Your open key: {}.\nYour secret key: {}.\nEncrypted text: {}'.format(openkey, secretkey, encryptiontext)
    send_mail(subject, message, 'pch.new123@gmail.com', [email])

    context = {'encryptiontext': encryptiontext,
               'openkey': openkey,
               'secretkey': secretkey,
               'email': email,
               'usertext': usertext,
               }
    return render(request, 'encryption/success.html', context=context)
