import pyttsx3

txv = pyttsx3.init()

voices = txv.getProperty('voices')
txv.setProperty('voice', voices[0].id)
txv.setProperty('rate', 150)

text = "1234567891011121314151617181920"

txv.say(text)
txv.runAndWait()
