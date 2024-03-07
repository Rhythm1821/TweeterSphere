from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Profile,Tweet
from .forms import TweetForm,RegisterForm,ProfileImageForm,UserUpdateForm

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

def register(request):
    form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'You are registered')
            return redirect('home')
        
    return render(request,'register.html',{'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = UserUpdateForm(request.POST or None,request.FILES or None,instance=current_user)
        profile_form = ProfileImageForm(request.POST or None,request.FILES or None,instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            print("Valid")
            user_form.save() and profile_form.save()
            login(request,current_user)
            messages.success(request,"Your profile has been updated")
            return redirect('home')
        return render(request,'update_user.html',{'user_form':user_form,'profile_form':profile_form})
    else:
        messages.error(request,"You must be logged in!")
        return redirect('home')
    

def tweet_like(request,pk):
    if request.user.is_authenticated:
        tweet = get_object_or_404(Tweet,id=pk)
        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user.id)
        else:
            tweet.likes.add(request.user.id)
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request,"You must be logged in!!")
        return redirect('home')

def tweet_show(request,pk):
    tweet = get_object_or_404(Tweet,id=pk)
    if tweet:
        return render(request,'show_tweet.html',{'tweet':tweet})
    else:
        messages.error(request,'Tweet does not exist!!')
        return redirect('home')
    
def unfollow(request,pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=pk)
        request.user.profile.follows.remove(profile)
        request.user.profile.save()
        messages.info(request,f'{profile.user.username} unfollowed')
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.success(request,'You are not logged in!!')
        return redirect('home')