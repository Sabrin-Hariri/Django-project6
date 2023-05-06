import http
from django.shortcuts import render
from django.contrib.auth.views import  LoginView 
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin # save your page 
from .forms import *
from django.contrib.auth import login
from django.shortcuts import redirect

#############################

class Home(TemplateView):

    template_name = "home.html"


## cont show profile page without login
class ProfileViews(LoginRequiredMixin,TemplateView):
    template_name = "profile.html"    


class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user=True ### يما انو مسجل ما فيك تشوف صفحه اللوجن   
    def get_success_url(self):
        messages.info(self.request,'welcome' )
        return reverse_lazy('profile')
    def form_invalid(self , form):
        messages.error(self.request,'error info ' )
        return self.render_to_response( self.get_context_data(form = form))


class Register(FormView):
    template_name = "register.html"
    form_class=RegisterationForm
    success_url= reverse_lazy('profile')
    redirect_authenticated_user=True ### يما انو مسجل ما فيك تشوف صفحه اللوجن   
    
    ### if you have account -->take you to profile page
    def dispatch(self, request ,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super(Register,self).dispatch(request, *args, **kwargs)
    
    def form_valid(self,form):
        user = form.save()
        messages.info(self.request,'welcome' )

        if user:
            login(self.request,user)
        return super(Register,self).form_valid(form)

 