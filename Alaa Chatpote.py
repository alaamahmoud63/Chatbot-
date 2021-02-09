#this is an Input/Output AI Chatbot based on Manual Rules 

import os 
os.system('color 3f') #sets the background to blue

#make python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

#start the conversation
print('Hi Mate!') #greething
speak.Speak('Hi Mate!')

#KEEP Going the conversation 
print('Whats your name?') #ask
speak.Speak('Whats your name?')
Name = input() #save answer
print('Im glad to meet you,' + Name + '!!') #replay
speak.Speak('Im glad to meet you,' + Name + '!!')
print('the number of letters of you name is:')
speak.Speak('the number of letters of you name is:')
print(len(Name))
speak.Speak(len(Name))

#Keep going the conversation 
print('How old are you?')#ask
speak.Speak('How old are you?')
Reply = input() #save answer 
print('Okay, then you will be' + str(int(Reply) + 1) + 'next year.')#reply 
speak.Speak('Okay, then you will be' + str(int(Reply) + 1) + 'next year.')

#Keep going the conversation
print('Whats the name of your brother?') #ask
speak.Speak('Whats the name of your brother?')
Reply = input() #save answer
print('Awesome!, my brother name is also ' + Reply + '!!')
speak.Speak('Awesome!, my brother name is also ' + Reply + '!!')

#keep going the convertsation 
print('whats your aunts Name')
speak.Speak('whats your aunt Name')
Reply = input() #save answer
print('Ah ha! I do not have any aunt Whose name is' + Reply)#reply
speak.Speak('Ah ha! I do not have any aunt Whose name is' + Reply)

#Keep going the conversation 
print('And do you have an aunt named AShowk') #reply
speak.Speak('And do you have an aunt named is Ashwak')
Reply = input() #save answer 
print('Okay,Ihave 2 aunts Whose name is Ashowk')#reply
speak.Speak('Okay,Ihave 2 aunts Whose name is Ashowk')

#Keep going conversation
print('By the way, are you enjoying this conversation?') #ask
speak.Speak('By the way, are you enjoying this conversation?')
Reply = input() #save answer
print('oh nice ,me too. Ineeded to talk to someone,even if its just a human. Although the machines give me more game! Just Kidding' + Name + '!!') #reply
speak.Speak('oh nice ,me too. Ineeded to talk to someone,even if its just a human. Although the machines give me more game! Just Kidding' + Name + '!!')


#Keep going the conversation
print('can you lend me your new car?') #ask
speak.Speak('can you lend me your new car?')
Reply = input() #save answer
print('Oh,well, tomorrow ill pick it up early. perfect,Well talk tomorrow when Icame back. Bye' + Name) #reply
speak.Speak('Oh,well, tomorrow ill pick it up early. perfect,Well talk tomorrow when Icame back. Bye' + Name)














