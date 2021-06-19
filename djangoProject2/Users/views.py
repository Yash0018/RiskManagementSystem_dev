from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import LogInForm, Clientdoc
from .models import Document, Client_Profile, Consultant_Profile, Event

user_details = [
    {
        # in future documents[] will return path related to given client.
        # this list of file path can be obtained with given id to documents table and adding client and consultant foreign key to it
        'id': '1',
        'name': 'name1',
        'email': 'name1@email.com',
        'DOB': '1-1-2001',
        'status': 'active-client',
        'documents': ['docs/client1/doc1', 'docs/client1/doc2', 'docs/client1/doc3', 'docs/client1/doc4'],
        'join_date': '1-2-2020',
    },
    {
        'id': '2',
        'name': 'name2',
        'email': 'name2@email.com',
        'DOB': '2-1-2001',
        'status': 'active-client',
        'documents': ['docs/client2/doc1', 'docs/client2/doc2', 'docs/client2/doc3', 'docs/client2/doc4'],
        'join_date': '1-2-2020',
    },
    {
        'id': '3',
        'name': 'name3',
        'email': 'name3@email.com',
        'DOB': '3-1-2001',
        'status': 'active-client',
        'documents': ['docs/client3/doc1', 'docs/client3/doc2', 'docs/client3/doc3', 'docs/client3/doc4'],
        'join_date': '1-2-2020',
    },
    {
        'id': '001',
        'name': 'consultant1',
        'email': 'consultant1@email.com',
        'DOB': '1-1-2001',
        'status': 'active-consultant',
        'documents': ['docs/consultant1/doc1', 'docs/consultant1/doc2', 'docs/consultant1/doc3', 'docs/consultant1/doc4'],
        'join_date': '1-2-2020',
    },
    {
        'id': '002',
        'name': 'consultant2',
        'email': 'consultant2@email.com',
        'DOB': '1-1-2001',
        'status': 'active-consultant',
        'documents': ['docs/consultant2/doc1', 'docs/consultant2/doc2', 'docs/consultant2/doc3', 'docs/consultant2/doc4'],
        'join_date': '1-2-2020',
    },

]


def user(request):
    # bellow context will be used when we query data from database instead of dummy data
    """
    context = {
        'user_details': Document.objects.all(),
        'title': 'user'
    """
    context = {
        'user_details': user_details,
        'title': 'user'
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def loginpage(request):
    logoutfunction(request)
    form = LogInForm(request.POST)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user1 = Client_Profile.objects.filter(user_id=request.user).exists()
            if user1:
                return redirect('client-home-page')  # it uses the name mentioned in url.py file
            else:
                # user2 = Consultant_Profile.objects.get(user_id=request.user)
                return redirect('consultant-home-page')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login-page')
    context = {'form': form}
    return render(request, 'login_page.html', context)


@login_required
def client_home(request):
    client_pr = Client_Profile.objects.get(user_id=request.user)
    events = Event.objects.filter(client_id=client_pr.pk).prefetch_related('document_set')
    context = {'events': events, 'client_pr': client_pr}
    return render(request, 'Client/client_index.html', context)


@login_required
def consultant_home(request):
    consultant_pr = Consultant_Profile.objects.get(user_id=request.user)
    events = Event.objects.filter(consultant_id=consultant_pr.pk).prefetch_related('document_set')
    context = {'events': events, 'consultant_pr': consultant_pr}
    return render(request, 'Consultant/consultant_index.html', context)


@login_required
def client_upload(request):
    client_pr = Client_Profile.objects.get(user_id=request.user)
    form = Clientdoc(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            doc = form.save(commit=False)
            # doc.client_id = request.user
            doc.save()
            return redirect('client-home-page')  # it uses the name mentioned in url.py file
    return render(request, 'Client/client_upload.html', {'form': form, 'client_pr': client_pr})

@login_required
def consultant_upload(request):
    consultant_pr = Consultant_Profile.objects.get(user_id=request.user)
    form = Clientdoc(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            doc = form.save(commit=False)
            # doc.client_id = request.user
            doc.save()
            return redirect('consultant-home-page')
    return render(request, 'Consultant/consultant_upload.html', {'form': form, 'consultant_pr': consultant_pr})

@login_required
def logoutfunction(request):
    logout(request)
    return redirect('login-page')
