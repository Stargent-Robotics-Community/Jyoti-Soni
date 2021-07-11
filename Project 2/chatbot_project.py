import re
import pyttsx3
import speech_recognition as sr
import pyaudio

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
           audio=r.listen(source)
           r.adjust_for_ambient_noise(source)
           r.pause_threhold=1
    return audio

def get_text_message(audio):
    r=sr.Recognizer()
    try:
       text= r.recognize_google(audio)
       return text
    except:
       return "could not recognise"

def message_probability(user_message,recognised_words, single_response=False,required_words=[]):
    message_certainity = 0
    has_required_word=True

    for word in user_message:
        if word in recognised_words:
            message_certainity+=1

    percentage= float(message_certainity)/ float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_word = False
            break

    if has_required_word or single_response:
        return int (percentage*100)
    else:
        return 0


def cheak_all_messages(message):
        highest_prob_list = {}                            


        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response]= message_probability(message,list_of_words,single_response,required_words=[])  

    
        response("i am sorry would you mind saying it again",['could','not','recognise'],single_response=True)
        response('ok i will be back after several minutes',['no','now','not','thankyou','nothing else'],required_words=['no','thankyou','nothing else'])
        response('we have the best Indian Cuisine desert and coffee' ,['what','resturant','is','famous','special'],required_words=['special','resturant','famous'])
        response('would you like something to drink', ['i','will','like','have','order'],required_words=['order','like','will','have'])
        response('Thank you',['wonderful','love','good','nice'],required_words=['wonderful','love','good','nice'])
        response('yes surely we have', ['you','do','have','in','the ','restaurant','can',' i',' get'],required_words=['do','you','have','can',' i',' get'])
        response('yes are you ready to give your order ',['excuse','me','hey ','listen','order'],required_words=['excuse','me','hey '])
        response('would you like to have something in desert',['yes','have','i','will','order','like'],required_words=['yes','have','order','like'])
        
        best_match = max(highest_prob_list,key=highest_prob_list.get)    
    


        return  best_match


def get_audio_response(bot_answer):
    a=pyttsx3.init()
    a.say(bot_answer)
    a.runAndWait()
  

def wel_come():
    a=pyttsx3.init()
    a.say("Welcome to the resturant")
    a.say("What would you like to order?")
    a.runAndWait()



wel_come()

while True:
    audio=listen()
    text=get_text_message(audio)

    if text=='could not recognise':
             print('you:  ')
    else: 
             print('you: '+text) 

    split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
    bot_answer=cheak_all_messages(split_message)
    get_audio_response(bot_answer)
    print('bot: '+bot_answer)
  



