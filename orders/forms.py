from django import forms
from django.utils.translation import ugettext_lazy as _
from orders.models import ODOrder
from orders.models import Detcus


class ODOrderForm(forms.ModelForm):
    """
    Form to manage Order data-entry
    """
    name = forms.CharField(label=_('Nama Produk'))

    class Meta:
        model = ODOrder
        fields = ('name', 'phone', 'price')

class NCustomerForm(forms.ModelForm):
	"""
	Form for create new customer
	"""
	name = forms.CharField(label=_('Nama customer'))

	class Meta:
		model = Detcus
		fields = ('name', 'email', 'phone', 'address')