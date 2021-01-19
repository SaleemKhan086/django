from django.forms import ModelForm
from .models import Password

class RecordForm(ModelForm):
    class Meta:
        model=Password
        #fields='__all__'
        exclude=['owner',]
