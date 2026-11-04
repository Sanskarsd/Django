from django import forms

from reviews.models import Review

# class ReviewForm(forms.Form):
#     username=forms.CharField(label="Your Name", max_length=20, min_length=3, error_messages={
#         "required": "Please enter your name",
#         "min_length": "Your name is too short",
#         "max_length": "Your name is too long"
#     })
#     password=forms.CharField(label="Your Password", max_length=20, min_length=3, error_messages={
#         "required": "Please enter your password",
#         "min_length": "Your password is too short",
#         "max_length": "Your password is too long"
#     })

#     review_text=forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=500, min_length=10, error_messages={
#         "required": "Please enter your feedback",
#         "min_length": "Your feedback is too short",
#         "max_length": "Your feedback is too long"
#     }
#     )

#     rating=forms.IntegerField(label="Your Rating", min_value=1, max_value=5, error_messages={
#         "required": "Please enter your rating",
#         "min_value": "Please enter a valid rating",
#         "max_value": "Please enter a valid rating"
#     })


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["username", "password", "review_text", "ratings"]
        labels = {
            "username": "Your Name",
            "password": "Your Password",
            "review_text": "Your Feedback",
            "ratings": "Your Rating",
        }
        error_messages = {
            "username": {
                "required": "Please enter your name",
                "min_length": "Your name is too short",
                "max_length": "Your name is too long",
            },
            "password": {
                "required": "Please enter your password",
                "min_length": "Your password is too short",
                "max_length": "Your password is too long",
            },
            "review_text": {
                "required": "Please enter your feedback",
                "min_length": "Your feedback is too short",
                "max_length": "Your feedback is too long",
            },
            "ratings": {
                "required": "Please enter your rating",
                "min_value": "Please enter a valid rating",
                "max_value": "Please enter a valid rating",
            },
        }
