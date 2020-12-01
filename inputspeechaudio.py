# pyttsx3 module i sspecially for the speech reader or data reader
import pyttsx3
friend = pyttsx3.init()
# this input is used to make ur pc speak as what u required to get output as speech
speech = input("say something:")
# here say is abt generally giving to out
friend.say(speech)
friend.runAndWait()
