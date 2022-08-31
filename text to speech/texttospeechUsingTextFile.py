from gtts import gTTS

# This module is imported for text to speech coversion
import os
abc = open('sample.txt')
# The text that you want to convert to audio
mytext =abc.read() #'hello guys,I am mahalakshmi born and raised in hyderabad'
# Language in which you want to convert
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")