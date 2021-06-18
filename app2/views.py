# django imports
from django.views.generic.edit import FormView
from django.http import HttpResponse

# custom imports
from .forms import ReviewForm

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "<h1>Thanks for the review!</h1>"
        return HttpResponse(msg)
