from django import forms

class FeedbackForm(forms.Form):
    CHOICES = (('M', 'Male'),('F', 'Female'),)
    name = forms.CharField(label='First name', min_length=2, max_length=15, error_messages={
        'max_lenght': 'Too many characters',
        'min_lenght': 'Too few characters',
        'required' : 'This field is required'
    })
    surname = forms.CharField()
    gender = forms.ChoiceField(choices=CHOICES)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20}))
    rating = forms.IntegerField(label='Rating', max_value=10, min_value=1)