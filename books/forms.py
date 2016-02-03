from django import newforms as forms

TOPIC_CHOICES = (
  ('general', 'General enquiry'),
  ('bug', 'Bug report'),
  ('suggestion', 'Suggestion')
)

class ContactForm (forms.form):
  topic = forms.ChoiceField(choices=TOPIC_COICES)
  message = forms.CharField(widget=forms.Textarea())
  sender = forms.EmailField(required=False)
