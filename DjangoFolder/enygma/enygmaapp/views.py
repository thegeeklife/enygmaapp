from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from enygmaapp.forms import UserForm, UpdateUserForm
import os
import requests
import environ
env = environ.Env()
environ.Env.read_env()

# Index/Homepage file.
#context is provided so that it's easy to edit.
def index(request):
	context = {
	'subtitle':'An online mystery solving social platform',
	'description_paragraphs':[
		'This platform presents several mystery options for you to choose from. If you enjoy a good spook and solving seemingly supernatural mysteries, check out our horror category. If you enjoy solving like a detective, we have a hardboiled category where you investigate the case like a deetctive. If your passion is being a private detective, you should get an idea of what that is like by checking out our noir category.',
		'Throughout this experience you will look for clues, identify potential suspects and their motives. You can also use the discussion section to discuss any theories you may have with other slueths on our platform!',
	],
	}


	#Setting empty session (Notion tutorial)
	logged_in= request.session.get("logged_in",False)
	username = request.session.get("username","guest")

	return render(request, 'enygmaapp/homepage.html', context)
	# return HttpResponse("Hello, welcome to the enygma app.")

#The pages that do not work yet will be redirected to default 404 not found error
def default(request):
	context = {}
	return render(request, 'enygmaapp/default.html', context)

#This will display items in the collection
def items(request):

	#defining data in json format
	context = {
		'genres':['Horror', 'Hardboiled', "Noir"],
		'difficulties': ['Easy', 'Hard'],
		'featured_list':[
			{
			'img': "https://images.pexels.com/photos/685674/pexels-photo-685674.jpeg?auto=compress&cs=tinysrgb&w=800",
			'title': 'Murder Vendetta',
			'mysteryid':'1'},
			{
			'img': 'https://images.pexels.com/photos/3144296/pexels-photo-3144296.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'The College Girl',
			'mysteryid':'2'},
			{
			'img':'https://images.pexels.com/photos/2901916/pexels-photo-2901916.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Model Goes Missing',
			'mysteryid':'0'},
			{
			'img': 'https://images.pexels.com/photos/3274899/pexels-photo-3274899.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Middle of Mountains',
			'mysteryid':'3'},
			{
			'img':'https://images.pexels.com/photos/1516191/pexels-photo-1516191.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'The Diver',
			'mysteryid':'4'},
			{
			'img':'https://images.pexels.com/photos/547593/pexels-photo-547593.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Magic Show Mystery',
			'mysteryid':'5'},
			],

		'horror_list':[
			{
			'img': "https://images.pexels.com/photos/2927707/pexels-photo-2927707.jpeg?auto=compress&cs=tinysrgb&w=800",
			'title': 'Ashes at Asylum',
			'mysteryid':'6'},
			{
			'img': 'https://images.pexels.com/photos/3993249/pexels-photo-3993249.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Haunted Tent',
			'mysteryid':'7'},
			{
			'img':'https://images.pexels.com/photos/6691395/pexels-photo-6691395.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Masked Mannequin',
			'mysteryid':'8'},
			{
			'img': 'https://images.pexels.com/photos/5696525/pexels-photo-5696525.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Seance Killer',
			'mysteryid':'9'},
			{
			'img':'https://images.pexels.com/photos/5859666/pexels-photo-5859666.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Corpse Bride',
			'mysteryid':'10'},
			{
			'img':'https://images.pexels.com/photos/7189111/pexels-photo-7189111.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Cult Crimes',
			'mysteryid':'11'},
			],
		'hardboiled_list':[
			{
			'img': "https://images.pexels.com/photos/333525/pexels-photo-333525.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
			'title': 'Plane Disappearance',
			'mysteryid':'12'},
			{
			'img': 'https://images.pexels.com/photos/258420/pexels-photo-258420.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			'title':'Last Seen Subway',
			'mysteryid':'13'},
			{
			'img':'https://images.pexels.com/photos/7991500/pexels-photo-7991500.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			'title':'Murder at the Movies',
			'mysteryid':'14'},
			{
			'img': 'https://images.pexels.com/photos/2901916/pexels-photo-2901916.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Model Goes Missing',
			'mysteryid':'0'},
			{
			'img':'https://images.pexels.com/photos/42240/pexels-photo-42240.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			'title':'Chestnut Cottage',
			'mysteryid':'16'}
			],

		'noir_list':[
			{
			'img': "https://images.pexels.com/photos/690816/pexels-photo-690816.jpeg?auto=compress&cs=tinysrgb&w=800",
			'title': 'The Stolen Scooter',
			'mysteryid':'17'},
			{
			'img': 'https://images.pexels.com/photos/3144296/pexels-photo-3144296.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'The College Girl',
			'mysteryid':'18'},
			{
			'img':'https://images.pexels.com/photos/5378963/pexels-photo-5378963.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'The Affair',
			'mysteryid':'45'},
			{
			'img': 'https://images.pexels.com/photos/9183306/pexels-photo-9183306.jpeg?auto=compress&cs=tinysrgb&w=800',
			'title':'Vacation Blues',
			'mysteryid':'19'},
			{
			'img':'https://images.pexels.com/photos/7266011/pexels-photo-7266011.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			'title':'Man with Scar',
			'mysteryid':'20'}
			]
	}


	return render(request, 'enygmaapp/items.html', context)

# The detail view page
def mystery_title(request, mysteryid):
    context={
	   'mystery_details':{
			'mysteryid':'0',
			'mystery_title': 'Model Goes Missing',
			'likes':'22',
			'dislikes':'3',
			'genre': 'Hardboiled',
			'difficulty': 'Easy',
			'percentage_solved':'25',
			'storyparagraphs': '<p> On a cold September night, Jendall Kenner was taking the subway back to her apartment. Being a model in her early 20\'s, she struggled with making enough money to pay her rent in a big expensive city like New York and taking a cab was not an option. Jendall grew up in a middle class family that moved constantly due to her mother\'s several temp jobs. She had to look after siblings when she was younger, but eventually decided to help her mother make more money to help her in clearing off debts. </p> <p> One person that constantly stayed by Jendall\'s side was her childhood best friend Alex, who was now a realtor in Manhattan. He offered to loan her money several times, but Jendall always refused to take money from him. She always had an intuition that it would not be wise to do so, mostly because she always had noticed that his eyes lingered. She was used to ignoring this behavior now however as she realized this was the case with any woman Alex interacted with. Perhaps, she was overthinking this? Alex was a good person after all, he always helped her baby sit her siblings and even watched them for her when she snuck out to meet the boys she dated. She did however wonder why Alex never introduced her to the girls he dated. On her way home from her job that night, she thought to reach out to Alex and see if he would like to hang out over the weekend. Jendall was not a party girl unlike Alex, but she did enjoy a good drink every once in a while. </p> <p> She was still walking on the subway thinking about calling Alex, when someone grabbed her, covering her mouth in an attempt to make her unconscious. However, Jendall was a smart girl and she had her pepper spray on her, which she did not hesitate to use. Once her assaulter let go of her due to the irritation in his eyes, she quickly ran to alert security and took an uber home. She was mortified and she called  Alexright away, who later picked her up and took her back to his place so she would not be alone. He had a nice apartment in downtown Manhattan by Times Square. </p> <p> The next morning, Jendall was supposed to be at work, but never showed up. Her manager Esteban tried to contact her, but to no avail. This was quite unlike Jendall, Esteban thought, but he realized something must have come up and decided to give Jendall some time. Later that night, Alex tried to contact Jendall to see if she needed a ride back to his place or her place, but she didn\'t answer. Alex contacted Esteban to ask about Jendall, but he was told that she didn\'t show up to work. Alex thought that she probably went to see her colleague Lisa for some emotional support, but when he called her, she said she hadn\'t heard from Jendall either. </p>',
			'suspects':['Lisa', 'Alex', 'Esteban'],
			'motives':['Money', 'Jealousy', 'Accidentally'],
			'discussions':[
				{
					'user': 'stormbreaker',
					'comment': 'I think Alex is the murderer because she was the last person to see Jendall alive.',
					'replies': 'siennasings: I agree!!',
					'commentlikes': '10',
					'commentdislikes':'1',
				},
				{
					'user': 'sluethhead',
					'comment': 'I think it was Lida, she is probably jealous of Jendall\'s successful career and killed her.',
					'replies': 'arthurisbest: That sounds like garbage.',
					'commentlikes': '3',
					'commentdislikes':'1',
				},
			             ]
		          }
    }
    # return render(request,"enygmaapp/myprofile.html",context["post_data"])
    if request.method=="POST":
        context["post_data"] = request.POST
        term = request.POST['wordsearch']
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":term}
        key = os.environ.get('key')
        headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
        }
        my_response = requests.request("GET", url, headers=headers, params=querystring)
        my_response_json = my_response.json()
        context = {
            'def': my_response_json['list'][1]['definition'],
            'search': my_response_json['list'][1]['word'],
            'author': my_response_json['list'][1]['author'],
            'sentence': my_response_json['list'][1]['example'],
            'thumbs_up': my_response_json['list'][1]['thumbs_up'],
            'thumbs_down': my_response_json['list'][1]['thumbs_down']
        }
        print(context)
        return render(request, 'enygmaapp/definition.html', context)
    return render(request, 'enygmaapp/mysterytitle.html', context)

# The add an item page that uses post method to post data
def create_mystery(request):
	context = {
		'selected_genre':'Horror',
		'totalclues':'3',
		'story': 'abcd',
		'totalsuspects':'',
		'sus1': '',
		'sus2':'',
		'sus3':'',
		'sus4':'',
		'mot1':'',
		'mot2':'',
		'mot3':'',
		'mot4':'',
		'selectedculprit':'',

	}

	if request.method == "POST":
		context["post_data"] = request.POST
		print(context["post_data"])
		selected_genre = request.POST['selected_genre']
		totalclues = request.POST['totalclues']
		story = request.POST['story']
		totalsuspects = request.POST['totalsuspects']
		sus1 = request.POST['sus1']
		sus2 = request.POST['sus2']
		sus3 = request.POST['sus3']
		sus4 = request.POST['sus4']
		mot1 = request.POST['mot1']
		mot2 = request.POST['mot2']
		mot3 = request.POST['mot3']
		mot4 = request.POST['mot4']
		selectedculprit = request.POST['selectedculprit']
	# 	#context["username"] = request.POST['username']
		return render(request,"enygmaapp/selectclues.html",context["post_data"])

	return render(request, 'enygmaapp/createmystery.html', context)

# def select_culprit(request):
# 	context	= {
# 		'totalsuspects':'',
# 		'sus1': '',
# 		'sus2':'',
# 		'sus3':'',
# 		'sus4':'',
# 		'mot1':'',
# 		'mot2':'',
# 		'mot3':'',
# 		'mot4':'',
# 		'selectedculprit':'',
# 	}
# 	if request.method == "POST":
# 		context["post_data"] = request.POST
# 		print(context["post_data"])
# 		totalsuspects = request.POST['totalsuspects']
# 		sus1 = request.POST['sus1']
# 		sus2 = request.POST['sus2']
# 		sus3 = request.POST['sus3']
# 		sus4 = request.POST['sus4']
# 		mot1 = request.POST['mot1']
# 		mot2 = request.POST['mot2']
# 		mot3 = request.POST['mot3']
# 		mot4 = request.POST['mot4']
# 		selectedculprit = request.POST['selectedculprit']
# 	# 	#context["username"] = request.POST['username']
# 		return render(request,"enygmaapp/selectclues.html",context["post_data"])
#
# 	return render(request, 'enygmaapp/selectculprit.html', context)


# Select clues and display data from previous form
def select_clues(request):
	context = {
		'story': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
	}
	return render(request, 'enygmaapp/selectclues.html', context)

# Login page
def loginpage(request):
	context={}

	#using the sign in form
	context["request_method"] = request.method
	username = "guestuser100"
	password="123"
	if request.method == "POST":
		context["post_data"] = request.POST
		username = request.POST['username']
		password=request.POST['password']
		request.session['logged_in'] = True
		request.session['username'] = username
		request.session['password'] = password
		print(request.session['logged_in'])

		#context["username"] = request.POST['username']
		return redirect("/enygmaapp/items")
		#return JsonResponse(context)

	#using cookies, this is based on the tutorial on notion
	print(request.COOKIES)

	username = "guestuser100"

	if request.method == "POST":
		username = request.POST['username']
	resp = render(request, 'enygmaapp/login.html', context)
	resp.set_cookie("guestuser100",username)
	resp.set_cookie("foo","bar",max_age=3600)

	#to implement session functions, again based on tutorial on notion
	num_visits = request.session.get("num_visits",0) + 1
	request.session['num_visits'] = num_visits
	if num_visits > 4: del(request.session['num_visits'])
	print(request.session.keys())
	if 'num_visits' not in request.session.keys():
		return render(request, 'enygmaapp/homepage.html', context)

	#Setting empty session (Notion tutorial)
	logged_in= request.session.get("logged_in",False)
	username = request.session.get("username","guest")


	return render(request, 'enygmaapp/login.html', context)

#View your profile - uses get to display your data
def my_profile(request):
    data = User.objects.all()
    userdetails = {
        "userdetails":data
    }
	# context = {
	# 	 'username': 'guestuser100',
	# 	 'firstname': 'guest',
	# 	 'lastname': 'user',
	# 	 'emailaddress': 'guestuser100@abcd.com',
	# }
    return render(request, 'enygmaapp/myprofile.html', userdetails)

#Edit the profile (editable method that uses post to send data)
def edit_profile(request):
	# context = {
	# 	'username': 'subiaansari',
	# 	'firstname': 'Subia',
	# 	'lastname': 'Ansari',
	# 	'emailaddress': 'subia.ansari96@gmail.com',
	# }
    data = User.objects.all()
    context = {
        "userdetails":data
    }
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Successfully updated')
            return render(request, "enygmaapp/my_profile.html", {'user_form':user_form})
    else:
        user_form = UpdateUserForm(request.POST)
        # context["post_data"] = request.POST
        # username = request.POST['username']
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        # emailaddress = request.POST['emailaddress']
        #return render(request,"enygmaapp/myprofile.html",context["post_data"])
    return render(request, 'enygmaapp/editprofile.html', {'user_form':user_form})

def signout(request):
    logout(request)
    print(request.user)
    return redirect('/Assignment4/')

def signin(request):
	if request.method == "GET":
		return render(request, "enygmaapp/login.html", {})
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect("/enygmaapp/items")
	else:
		return HttpResponse("Invalid Login")

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created, please log in.')
            return redirect('/enygmaapp/signup')
    else:
        form = UserForm()

    return render(request, 'enygmaapp/signup.html', {'form':form})

def delete_user(request, username):
    u = User.objects.get(username=username)
    u.delete()
    return redirect('/enygmaapp/signup')
