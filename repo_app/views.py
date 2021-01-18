from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from repo_app.models import MyUser, Image
from repo_app.forms import SignUpForm, UploadForm, LoginForm

class Index(View):
    def get(self, request):
        html = 'index.html'
        images = list(Image.objects.all().values())
        
        # for file in images:
        #     print(file[1])
        context = {'images': images}
        return render(request, html, context)

class Upload(View, LoginRequiredMixin):
    form_class = UploadForm
    def get(self, request):        
        html = 'upload.html'
        form = self.form_class()
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data            
            image = data['image']
            author = MyUser.objects.get(id=request.user.id)        
            Image.objects.create(
                upload = image,
                author = author
            )        
        else:
            return redirect('/upload/')       
        return HttpResponseRedirect(reverse('home'))

class SignUp(View):
    form_class = SignUpForm
    def get(self, request):
        html = 'sign_up.html'
        form = self.form_class()
        context = {'form': form}
        return render(request, html, context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            new_user = MyUser.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('success'))

def success(request):
    html = 'success.html'
    return render(request, html)

class Login_View(View):
    form_class = LoginForm
    def get(self, request):
        html = 'login.html'
        form = self.form_class()
        context = {'form': form}
        return render(request, html, context)
    
    def post(self, request):
        form = self.form_class(request.POST)        
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(
                request, username=username, password=password
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("home")))
            else:
                return redirect('/login/')
                


class Profile(View, LoginRequiredMixin):
    def get(self, request, user_id):
        user = MyUser.objects.get(id=user_id)
        images = Image.objects.all()
        html = 'profile.html'
        context = {'user': user, 'images': images}
        return render(request, html, context)

def logout_view(request):
    logout(request)
    return redirect('home')