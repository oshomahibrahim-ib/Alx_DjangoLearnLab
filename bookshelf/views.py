from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class SignUpView(CreateView):
    model = User
    fields = ("username", "password")
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
