from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

#from .models import WallPost

class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


def homepage(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = NewUserForm(request.POST)

        if form.is_valid():
            # Create a new user object populated with the data we are
            # giving it from the cleaned_data form
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )

            # As soon as our new user is created, we make this user be
            # instantly "logged in"
            auth.login(request, user)
            return redirect('/')

    else:
        # if a GET we'll create a blank form
        form = NewUserForm()

    context = {
        'form': form,
    }
    return render(request, 'home.html', context)


#Reroutes to the Questions page
def all_users(request):
    context = {}
    #old code: 
    # users = User.objects.all()
    # context = {
    #     'users': users,
    # }
    return render(request, 'questions.html', context)



# def user_feed(request, username):
#     user = User.objects.get(username=username)

#     if request.method == 'POST':

#         # Create a form instance and populate it with data from the request
#         form = PostForm(request.POST)

#         if form.is_valid():
#             # Create a new WallPost object populated with the data we are
#             # giving it from the cleaned_data form

#             WallPost.objects.create(
#                 username=username, # Create using the current username
#                 text=form.cleaned_data['text'],
#             )

#             # This will just redirect to the current page
#             return redirect(request.get_full_path())

#     else:
#         # if a GET we'll create a blank form
#         form = PostForm()

#     # We need to get all the posts for this user's username
#     posts = WallPost.objects.filter(username=username)

#     context = {
#         'first_name': user.first_name,
#         'last_name': user.last_name,
#         'email': user.email,
#         'username': username,
#         'form': form,s
#         'posts': posts,
#     }
#     return render(request, 'pages/feed.html', context)




# def delete_post(request, post_id):
#     # Fetch the right WallPost with the post_id, then delete it.
#     post = WallPost.objects.get(id=post_id)
#     post.delete()

#     # Cool trick to redirect to the previous page
#     return redirect(request.META.get('HTTP_REFERER', '/'))




# def update_post(request, post_id):
#     new_text = request.POST['text']

#     # Load post and then update with new_text
#     post = WallPost.objects.get(id=post_id)
#     post.text = new_text
#     post.save()

#     # Cool trick to redirect to the previous page
#     return redirect(request.META.get('HTTP_REFERER', '/'))

######### NEW FUNCTIONS ###############

def questions(request, username):
    print('I am at function questions')
    user = User.objects.get(username=username)
    context = {
        'username': username,
    }
    print('I am at function questions')
    return render(request, 'questions.html', context)

def search(request, username):
    print('I am at function search')
    user = User.objects.get(username=username)
    context = {
        'username': username,
    }
    print('I am at function search')
    return render(request, 'search.html', context)

def find_match(request):
    print('I am at function find_match')
    return render(request, 'find_people.html')
