from django import forms
from .models import *
from landing.models import Subscriber

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]  