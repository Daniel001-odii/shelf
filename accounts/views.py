from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.


class signupView(generic.CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy("login")
        template_name = "registration/signup.html"