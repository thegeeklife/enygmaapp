# enygmaapp

# Context of the App
The purpose of this project is to create a web application that will bring communities of sleuths together by breaking down geographical barriers and connecting them everywhere, giving them the ability to interact with others, discuss theories and work their way to a solution building off of each other’s ideas. 

A theme that is common across real life cold cases and solving mysteries leisurely is that a lot of papers, boards and evidence are looked at, this means physical requirements for space are large and it may exclude some people from being able to participate. It is also easy to misplace documents if they are not organized as well. These physical constraint issues can be addressed by using a web application.

# Use Cases
The following are the main actions a user can take:
- Create an account or log in using their socials (Google and Facebook)
-	Select a mystery to solve from the following categories: Horror, hardboiled (police investigation) and noir (private detective)
-	Highlight sentences to identify clues
-	Engage in discussions with other users
-	Like/dislike a mystery and a comment
-	Submit a comment
- Submit their own mysteries


# Functionalities Currently Offered
- Sign up using the sign up link. (create)
- Log in using the account created (Facebook & Google login do not work yet).
- There is one mystery story, you can like/dislike it and post a comment.
- You can search for a word while viewing the mystery (done using urbandictionary API).
- You can update your profile information (username, first name, last name and email) under My Profile option. (update, retreive)
- You can also delete your profile. (view)
 
# Hosted URL
- The hosted url is http://127.0.0.1:8000/enygmaapp
- Libraries used include: 
  - jquery 3.6
  - fontawesomefree. 
- Tutorials referred to: 
  - Notion : Connecting Django to Front End, handling sessions, Ajax demo. 
  - Errors handled using Stackoverflow.
-	All the required files and folders are included, but in case the mystery title page does not look proper, please follow these steps:
	Install fontawesome using the requirements.txt file and using terminal to run this command: 
	- python -m pip install -r requirements.txt
	- python manage.py collectstatic
	- python manage.py migrate
- Resources:
	- https://rapidapi.com/community/api/urban-dictionary
	- https://whitenoise.evans.io/en/stable/
