from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)  
from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)  
from django.urls import reverse 
from django.contrib.auth import get_user_model
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView) 
from .models import CustomUser

User = get_user_model()

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


class UserDetail(DetailView):
    model = CustomUser  
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user'  

class UserUpdate(UpdateView):
    model = CustomUser 
    form_class = UserUpdateForm  
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.kwargs['pk']})

class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

class UserDelete(DeleteView):
    model = CustomUser  # Usamos CustomUser en lugar de User
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('login')