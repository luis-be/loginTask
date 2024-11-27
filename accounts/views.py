from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        correo_electronico = form.cleaned_data.get("correo_electronico")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(correo_electronico=correo_electronico, password=raw_pw)
        login(self.request, user)
        return response