from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Profile,Tweet
from .forms import TweetForm

# Create your views here.
def home(request):
    tweets = None
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if request.method=="POST":
            if form.is_valid():
                tweet=form.save(commit=False)
                tweet.user=request.user
                tweet.save()
                messages.success(request,'Your tweet is Posted')
                return redirect('home')
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request,'home.html',{"tweets":tweets,"form":form})
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request,'home.html',{"tweets":tweets})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request,'profile_list.html',{'profiles':profiles})
    else:
        messages.success(request,'You must be logged in to view this...')
        return redirect('home')

def profile(request,pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk).order_by('-created_at')
        if request.method=='POST':
            # Get current user
            current_user_profile=request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action=='unfollow':
                current_user_profile.follows.remove(profile)
            elif action=='follow':
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return render(request,'profile.html',{'profile':profile,'tweets':tweets})
    else:
        messages.warning(request,'You must be logged in to view this...')
        return redirect('home')
    
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request=request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'You are logged in')
            return redirect('home')
        else:
            messages.error(request,'Either username or password is invalid')
            return redirect('login')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.info(request,"You are logged out!")
    return redirect('home')