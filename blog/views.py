from django.shortcuts import render
from django.utils import timezone
from .models import Post
from blog.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, REDIRECT_FIELD_NAME
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/user/home/')

def custom_login(request):
    if request.user.is_authenticated():
        if request.user.username == 'admin':
            return HttpResponseRedirect('/admin/')
        return HttpResponseRedirect('/user/home/')
    else:
        return login(request)

@login_required
def home(request):
    return render_to_response(
    'registration/home.html',
    { 'user': request.user }
    )

def post_list(request):
    posts = Post.objects.filter(
    	published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def blog_post(request):
    return render_to_response(
        'registration/blog_form.html',
        { 'user': request.user }
        )

@login_required
def user_post(request):
    # import ipdb; ipdb.set_trace()
    posts = Post.objects.filter(
        author_id=request.user.pk).order_by('published_date').reverse()
    return render_to_response(
        'registration/user_blogs.html',
        {'user': request.user,
         'posts': posts,
         'post_count': posts.count()}
        )

@login_required
def post(request):
    return render_to_response(
        'registration/post.html',
        { 'user': request.user }
        )
