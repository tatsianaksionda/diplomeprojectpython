from django.contrib import admin

from .models import *

class Data_encryptionAdmin(admin.ModelAdmin):
    list_display = ('email','user_text', 'open_key', 'encrypted_text')
    search_fields = ('open_key', 'email')
    list_filter = ('email',)

admin.site.register(Data_encryption, Data_encryptionAdmin)