from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .forms import ProfileUserChangeForm, UserRegisterForm


def index(request):
    return render(request, 'main/index.html')


@login_required
def profile(request):
    return render(request, 'profile/profile.html')


def edit(request):
    if request.method == 'POST':
        user_form = ProfileUserChangeForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
        return redirect('profile:profile')
    else:
        user_form = ProfileUserChangeForm(instance=request.user)
    return render(request, 'profile/edit.html', {'user_form': user_form})


def register_user(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
