from django.forms import ModelForm, Textarea, EmailInput
from .models import Data_encryption


class TextForm(ModelForm):
    class Meta:
        model = Data_encryption
        fields = ['email', 'user_text']
        widgets = {
            "user_text": Textarea(attrs={'class': 'usertext',
                                         'name': 'users_text',
                                         'maxlength': 1000,
                                         'required': True}),
            "email": EmailInput(attrs={'class': 'useremail',
                                       'placeholder': 'Enter your email',
                                       'required': True,
                                       'name': 'email_user'})
        }
