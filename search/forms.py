from django import forms
class FileForm(forms.Form):
    csv_file=forms.FileField()
