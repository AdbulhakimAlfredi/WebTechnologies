from django import forms
from .models import Book
from .models import Student, Address

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn_number']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line', 'city']

        class StudentForm(forms.ModelForm):
            class Meta:
              model = Student
              fields = ['name', 'age', 'addresses']  

    addresses = forms.ModelMultipleChoiceField(queryset=Address.objects.all(), widget=forms.CheckboxSelectMultiple)

class StudentImageForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['image']  