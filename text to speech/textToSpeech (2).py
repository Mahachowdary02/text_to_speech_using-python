from gtts import gTTS
#we have imported this model for  text to speech
import os
text = ' Hello guys ,I am O.Mahalakshmi  born and raised in Hyderabad '
#text which i want to covert
language = 'en'#en is english language
obj = gTTS(text = text, lang=language, slow=False)
obj.save("sample.mp3")