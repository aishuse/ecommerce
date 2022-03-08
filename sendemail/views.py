from django.http.response import HttpResponse
from django.views.generic import FormView
from sendemail.forms import ContactFormEmail
from .tasks import test_func
# Create your views here.


def test(request):
    test_func.delay()
    return HttpResponse("Done")
#
class SendEmail(FormView):
    template_name = "send_mail/contact.html"
    form_class = ContactFormEmail

    def form_valid(self, form):
        form.send_email()
        return HttpResponse("thanks for sending email")

