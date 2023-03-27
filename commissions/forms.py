from django import forms
from .models import Commission
from crispy_forms.helper import FormHelper


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ('full_name', 'email', 'phone_number', 'location',
                  'commission_request',)

