def create_youtube_video(title,descreption):
	dict = {'title':title,'descreption':descreption,'like':0,'dislike':0,"username":{"rami":"wdjiawdijawdijwijdaw"},"hashtag":["","","","",""]}
	for i in range(5):
		dict["hashtag"][i]= input("enter a hashtag")
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




def checksimilar(dict1,dict2):

	for x in range(5):
		c = 0 
		for i in range:
			if dict1["hashtag"][x] != dic2["hashtag"][i]:
				break
			else:
				c= c+1
		if c == 5 :
			print(5)











def check():
	dict = create_youtube_video('lol','this is my youtube video')
	like(dict)
	dislike(dict)
	print(dict['like'])
	print(dict['dislike'])
	print(dict['hashtag'])
	add_comment(dict,'rami11','I love this video')
	add_495(dict)
	print(dict['like'])
	print(dict['username'])

def add_495(dicionary):
	for  x in range(495):
		like(dicionary)





check()
