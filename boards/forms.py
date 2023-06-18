from django import forms
from .models import Topic
class NewTopicForm(forms.ModelForm):
    massage=forms.CharField(widget=forms.Textarea(
        attrs={'rows':5,'placeholder':'what is your massage?'}),
                help_text="The max lenght is 4000 charachter",
                max_length=4000)
    class Meta:
        model=Topic
        fields=['subject','massage']