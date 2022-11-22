from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from  django. urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm,ChangePasswordForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile
#from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

class UserProfilePage(generic.DetailView):
    model=Profile
    template_name='registration/user_profile_page.html'
    success_url=reverse_lazy('home')


    def get_context_data(self,*args,**kwargs):
        context = super(UserProfilePage,self).get_context_data(*args,**kwargs)
        user_profile= get_object_or_404(Profile, id=self.kwargs['pk'])
        context["user_profile"] = user_profile
        return context

class SignUpPage(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

def ProfilePage(request):
    return render(request,'registration/profile-page.html')

class EditProfile(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordChange(PasswordChangeView):
    form_class=ChangePasswordForm
    success_url=reverse_lazy('success-change')

def PwdChanged(request):
    return render(request,'registration/success-change.html')