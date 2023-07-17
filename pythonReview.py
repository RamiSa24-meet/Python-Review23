def create_youtube_video(title,descreption):
	dict = {'title':title,'descreption':descreption,'like':0,'dislike':0,"username":{}}

	return dict 


def like(dicionary):
	if 'like' in dicionary:
		dicionary['like'] = dicionary['like']+1
	return dicionary



def dislike(dicionary):
	if 'dislike' in dicionary:
		dicionary['dislike'] = dicionary['dislike']+1
	return dicionary

def add_comment(youtubename,username,comment_text):
	youtubename['username'][username]=comment_text


	return youtubename


def check():
	dict = create_youtube_video('lol','this is my youtube video')
	like(dict)
	dislike(dict)
	print(dict['like'])
	print(dict['dislike'])
	add_comment(dict,'rami11','I love this video')
	add_495(dict)
	print(dict['like'])
	print(dict['username'])

def add_495(dicionary):
	for  x in range(495):
		like(dicionary)





check()
