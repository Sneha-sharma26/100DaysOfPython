## Write a program to pronounce list of names using win32 API. If you are given a list of names. Program should pronounce :
# Shoutout to --name in list--

#---------Code--------#
# # without using 'pyttsx3'
# import win32com.client

# names = ['Sneha', 'Shruti', 'Kumkum', 'Kajal']
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# for name in names:
#         pronounce = f"Shoutout to {name}"
#         speaker.Speak(pronounce)  

# # with 'pyttsx3'
# import pyttsx3

# def shoutout_to_everyone(names : list) :
#     engine = pyttsx3.init()   # initialize the text-to-speech engine
    # for name in names:
    #     pronounce = f"Shoutout to {name}"
    #     engine.say(pronounce)   # It converts text to speech
#         engine.runAndWait()     # Wait until speech is finished
# name_list = ['Sneha', 'Shruti', 'Kumkum', 'Kajal']
# shoutout_to_everyone(name_list)