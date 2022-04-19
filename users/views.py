from pyexpat import model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from website.models import Post
from django.views import generic
from .forms import EditProfileForm



class UserList(generic.ListView):
    queryset = Post.objects.order_by('-uploaded_on')
    template_name = 'users/userPosts.html'
    
# ...
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'users/profile.html', {'profile': profile, 'user': user})



@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            firstName = form.cleaned_data["firstName"]#----new edit from here----#
            lastName = form.cleaned_data["lastName"]
            school = form.cleaned_data["school"]
            links = form.cleaned_data["links"]#----------to here-------#
            image = form.cleaned_data["image"]
            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            profile.firstName = firstName
            profile.lastName = lastName
            profile.school = school
            profile.links = links
            if image:
                profile.image = image
            profile.save()
            return redirect("users:profile", username=user.username)
    else:
        form = EditProfileForm(request.user.username)
    return render(request, "users/edit_profile.html", {'form': form})