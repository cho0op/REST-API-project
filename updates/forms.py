from django import forms
from .models import Update


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ['user', 'content', 'img']

    def clean(self):
        data = self.cleaned_data
        content = data.get('content', None)
        img = data.get("img", None)
        if content == "":
            content = None
        if content is None and img is None:
            raise forms.ValidationError("Enter content or img")
        return super().clean()
