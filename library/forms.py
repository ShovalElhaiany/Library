from django import forms
from django.forms import ModelForm
from library.models import Customer,Shop


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"
        

# books_choices=((1, "book1"),(2, "bbo2"))
# class ShopForm(forms.Form):
#     book_name = forms.MultipleChoiceField(books_choices, label="book"),
#     amount = forms.ChoiceField(label="amount")
class ShopForm(forms.Form):
    book_name = forms.MultipleChoiceField(),
    amount = forms.ChoiceField()
    

