from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Item
from datetime import datetime

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        def save(self, commit = True):
            user = super(NewUserForm, self).save(commit = False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

# class AddItemForm(forms.Form):
#     item_no = forms.CharField(help_text = "Enter Item Number ")
#     item_name = forms.CharField(help_text = "Enter Item Name ")
#     item_qty = forms.CharField(help_text = "Enter Item Quantity ")
#     item_price = forms.CharField(help_text = "Enter Quantity")
#     item_updated = forms.DateTimeField( initial = datetime.now())
#     item_desc = forms.CharField(widget = forms.Textarea)
#
#     def clean_item_no(self):
#         data = self.cleaned_data.get['item_no']
#         try:
#             match = Item.objects.get(item_no = data)
#         except Item.DoesNotExist:
#             return data
#         raise forms.ValidationError(_('Invalid Item Number - Item Number already Exists!!!'))
#
#     def clean_item_name(self):
#         data = self.cleaned_data.get['item_name']
#         try:
#             match = Item.objects.get(item_name = data)
#         except Item.DoesNotExist:
#             return data
#         raise forms.ValidationError(_('Invalid Item Name - Item Name already Exists!!!'))
#
#     def clean_item_qty(self):
#         data = self.cleaned_data.get['item_no']
#         return data
#
#     def clean_item_price(self):
#         data = self.cleaned_data.get['item_price']
#         return data
#
#     def clean_item_updated(self):
#         data = self.cleaned_data.get['item_updated']
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - updated in past'))
#         return data
#
#     def clean_item_desc(self):
#         data = self.cleaned_data.get['item_desc']
#         return data

class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = (
            'item_no', 'item_name', 'item_quantity', 'item_description', 'item_price'
        )

