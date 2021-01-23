from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'notice')
        widgets = {
            'notice': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        label and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['autofocus'] = True
        self.fields['body'].widget.attrs[
            'placeholder'] = "Type your comment here.."
        self.fields['body'].label = False
