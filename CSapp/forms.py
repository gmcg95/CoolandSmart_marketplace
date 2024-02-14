from django import forms
from .models import Message, OrderItem


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['lastname', 'firstname', 'email', 'phone', 'message']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
