from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

class SignupView(CreateView):
    form_class = SignupForm
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

# This made a password Error in my signup page

    # def form_valid(self, form):
    #     # Perform the authentication check
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']
    #     user = authenticate(self.request, username=username, password=password)

    #     if user is not None:
    #         # Credentials are valid, proceed with saving the user
    #         form.instance = user
    #         login(self.request, user)
    #         return super().form_valid(form)
    #     else:
    #         # Invalid credentials, handle accordingly
    #         error_message = 'Invalid username or password'
    #         form.add_error(None, error_message)
    #         return self.form_invalid(form)

def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {'user': user}
    return render(request, 'profile.html', context)