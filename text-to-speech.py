from gtts import gTTS
import os

# myText = 'ज्ञान सबका अधिकार है'
# language = 'hi'

myText = 'Welcome to DataSciPy. Source of free education'
language = 'en'

myobj = gTTS(text=myText, lang=language, slow=False)

myobj.save('myvoice.mp3')
os.system("myvoice.mp3")
