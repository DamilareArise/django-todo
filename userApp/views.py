from django.shortcuts import render
from .forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'
    
    
def ProfileView(request):
    userInfo = User.objects.get(id = request.user.id)
    profileInfo = Profile.objects.get(user_id=request.user.id)
    
    print(f'picture: {profileInfo.profile_picture}')
    
    return render(request, 'profile.html', {'userInfo': userInfo, 'profileInfo': profileInfo})