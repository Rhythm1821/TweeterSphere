from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
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

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request,'profile_list.html',{'profiles':profiles})

@login_required
def profile(request,pk):
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

@login_required
def update_user(request):
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = UserUpdateForm(request.POST or None,request.FILES or None,instance=current_user)
        profile_form = ProfileImageForm(request.POST or None,request.FILES or None,instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save() and profile_form.save()
            login(request,current_user)
            messages.success(request,"Your profile has been updated")
            return redirect('home')
        return render(request,'update_user.html',{'user_form':user_form,'profile_form':profile_form})
    
@login_required
def tweet_like(request,pk):
        tweet = get_object_or_404(Tweet,id=pk)
        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user.id)
        else:
            tweet.likes.add(request.user.id)
        return redirect(request.META['HTTP_REFERER'])


def tweet_show(request,pk):
    tweet = get_object_or_404(Tweet,id=pk)
    if tweet:
        return render(request,'show_tweet.html',{'tweet':tweet})
    else:
        messages.error(request,'Tweet does not exist!!')
        return redirect('home')

@login_required    
def unfollow(request,pk):
        profile = Profile.objects.get(user__id=pk)
        request.user.profile.follows.remove(profile)
        request.user.profile.save()
        messages.info(request,f'{profile.user.username} unfollowed')
        return redirect(request.META['HTTP_REFERER'])

@login_required    
def follow(request,pk):
        profile = Profile.objects.get(user__id=pk)
        request.user.profile.follows.add(profile)
        request.user.profile.save()
        messages.success(request,f'{profile.user.username} followed')
        return redirect(request.META['HTTP_REFERER'])

@login_required    
def followers(request,pk):
        if request.user.id==pk:
            profiles = Profile.objects.get(user__id=pk)
            return render(request,'followers.html',{'profiles':profiles})
        else:
            messages.error(request,"That's not your profile")
            return redirect('home')

@login_required    
def follows(request,pk):
        if request.user.id==pk:
            profiles = Profile.objects.get(user__id=pk)
            return render(request,'follows.html',{'profiles':profiles})
        else:
            messages.error(request,'')

@login_required    
def delete_tweet(request,pk):
        tweet = get_object_or_404(Tweet,id=pk)
        if request.user.username==tweet.user.username:
            tweet.delete()
            messages.info(request,'Tweet deleted...')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request,'You do not have the permission to delete the tweet!!')
            return redirect('home')

@login_required
def edit_tweet(request,pk):
        tweet = get_object_or_404(Tweet,id=pk)
        if request.user.username==tweet.user.username:
            form=TweetForm(request.POST or None,instance=tweet)
            if request.method=='POST':
                if form.is_valid():
                    tweet = form.save(commit=False)
                    tweet.user = request.user
                    tweet.save()
                    messages.success(request,'Tweet updated successfully')
                    return redirect('home')
            else:
                return render(request,'edit_tweet.html',{'tweet':tweet,'form':form})
        else:
            messages.error(request,'You are not authorized to edit this account')
            return redirect('home')

    
def search(request):
    if request.method=='POST':
        search = request.POST['search']
        searched = Tweet.objects.filter(body__contains=search)
        return render(request,'search.html',{'search':search,'searched':searched})
    else:
        return render(request,'search.html')

def search_user(request):
    if request.method=='POST':
        search = request.POST['search']
        searched = None
        if search:
            searched = User.objects.filter(username__contains=search)
        return render(request,'search_user.html',{'search':search,'searched':searched})
    else:
        return render(request,'search_user.html')