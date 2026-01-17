<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
>>>>>>> 5b29a6d (Complete relationship_app models and query samples)
