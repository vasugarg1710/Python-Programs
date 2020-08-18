import  requests
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch(“SAPI.SpVoice”)
    speak.Speak(str)


url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=c2380dd340a64dd791a032c9bf8ae286')
r = requests.get(url)
content = r.json()
arts = content['articles']
for title in arts:
    speak(title['title'])
    speak("Moving on to the next news")


