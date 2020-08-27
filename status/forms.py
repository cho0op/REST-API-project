from django import forms
from status.models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['user', 'content', 'image']

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get("content", None)
        image = data.get("image", None)
        if content == "":
            content = None
        if content is None and image is None:
            raise forms.ValidationError("content or img is required")
        return super().clean(*args, **kwargs)
