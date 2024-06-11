from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreateForm, CustomUserChangeForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})






