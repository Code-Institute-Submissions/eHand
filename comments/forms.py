from django import forms
from django.forms import Textarea
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'notice')
        widgets = {
            'notice': forms.HiddenInput(),
            'body': Textarea(attrs={'cols': 35, 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        label and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # this is dragging the page down on load - decide if required
        # self.fields['body'].widget.attrs['autofocus'] = True
        self.fields['body'].widget.attrs[
            'placeholder'] = "Type your comment here.."
        self.fields['body'].label = False
