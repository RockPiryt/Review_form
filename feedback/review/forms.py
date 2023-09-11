from django import forms
from .models import Review

class ReviewForm(forms.Form):
    pass
#     fuser_name = forms.CharField(label="Enter your name", max_length=100,  error_messages={
#         "required": "Your name must not be empty",
#         "max_lenght": "Your name must be shorter!",
#     })
#     freview_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     frating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class AutoReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        fields ='__all__'
        # exclude = ['owner_comment']
        labels = {
            "user_name": "Enter your name",
            "review_text": "Your Feedback",
            "rating": "Your rating",
        }
        error_messages = {
            "user_name":{
                "required":"Your name must not be empty!",
                "max_lenght": "Please enter a shorter name!"
            }
        }