import praw
import time
import os

#Login to Reddit
def bot_login():
	print("Logging in...")
	r = praw.Reddit(username =  os.environ.get('BOT_USERNAME', None), 
					password = os.environ.get('BOT_PASSWORD', None), 
					client_id = os.environ.get('BOT_ID', None),
					client_secret = os.environ.get('BOT_SECRET', None), 
					user_agent = "justinchuffy's akm converting bot v0.1")
	print("Logged in!")

	return r

#Run the bot
def run_bot(r):
	subreddit = r.subreddit("test+DallasFuel+NYXL+BostonUprising+FloridaMayhem+HoustonOutlaws+lagladiators+LAValiant+LondonSpitfire+PHL_Fusion+SeoulDynasty+SFShock_OW+ShanghaiDragons+OverwatchCirclejerk+OverwatchTMZ+Overwatchmemes+Overwatch_Memes+Overwatch+OverwatchLeague")
	print("Obtaining comments...")
	for comment in subreddit.stream.comments():
		with open("comments_replied_to.txt") as file:
			if "akm" in comment.body.lower() and comment.id not in file.read() and comment.author != r.user.me():
				with open("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")

				num = comment.body.lower().split("akm")[0].split()[-1]
				
				n = 0;
				isfloat = True
				try:
					float(num)
				except ValueError:
					isfloat = False
					break

				if isfloat == True:
					if num.isdigit() == True:
						n = int(num)
					else:
						n = float(num)

				calculate(n)
				print("String with \"akm\" found in comment " + comment.id)
				comment.reply(calculate(n) + "\n\n ___ ^(Beep boop. I am a bot that automatically converts) ^[aKm](https://i.redd.it/tr1uwg62rus01.gif) ^to ^time. ^PM ^[/u/Justinchuffy](https://www.reddit.com/user/justinchuffy) ^with ^issues ^or ^feedback!")
				print("Replied to " + comment.id)
				print("Sleeping for 5 seconds")
				time.sleep(5)

def calculate(n):
	converted = n * 224
	num = str(n)
	msg = num + " aKm is equal to "
	y = 0
	mo = 0
	w = 0
	d = 0
	h = 0
	m = 0
	s = 0

	if converted == 0:
		return (msg + "0 seconds")
	else:
		end = False
		while end == False:
			if converted >= 31536000:
				converted -= 31536000
				y += 1
			elif converted >= 2592000:
				converted -= 2592000
				mo += 1
			elif converted >= 604800:
				converted -= 604800
				w += 1
			elif converted >= 86400:
				converted -= 86400
				d += 1
			elif converted >= 3600:
				converted -= 3600
				h += 1
			elif converted >= 60:
				converted -= 60
				m += 1
			elif converted <= 60:
				s = converted
				end = True

		if y > 0:
			if y == 1:
				msg = msg + "%d year " % (y)
			else:
				msg = msg + "%d years " % (y)
		if mo > 0:
			if mo == 1:
				msg = msg + "%d month " % (mo)
			else:
				msg = msg + "%d months " % (mo)
		if w > 0:
			if w == 1:
				msg = msg + "%d week " % (w)
			else:
				msg = msg + "%d weeks " % (w)
		if d > 0:
			if d == 1:
				msg = msg + "%d day " % (d)
			else:
				msg = msg + "%d days " % (d)
		if h > 0:
			if h == 1:
				msg = msg + "%d hour " % (h)
			else:
				msg = msg + "%d hours " % (h)
		if m > 0:
			if m == 1:
				msg = msg + "%d minute " % (m)
			else:
				msg = msg + "%d minutes " % (m)
		if s > 0:
			if s == 1:
				msg = msg + "%d second " % (s)
			else:
				msg = msg + "%d seconds " % (s)

		return (msg)


r = bot_login()

while True:
	run_bot(r)
