import pygame
import sys
import speech_recognition as sr
from openai import OpenAI
import pyttsx3
import os
r=sr.Recognizer()


engine=pyttsx3.init()
engine.setProperty('voice', 'english-us')
def speak(say):
    engine.say(say)
    engine.runAndWait()

    
client = OpenAI(api_key=" Insert Open AI api key here ")
def chat_english():
    messages = [ {"role": "system", "content": 
              "I am going to use you as a translator. Google translate is bad, as its AI is not as advanced as you. I want you to take my english input and translate it into proper spanish and proper grammar. There should be no context or explanantion, just the translation"} ]

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('speak english')
            audio=r.listen(source)
            print('done')
            saidtxt=r.recognize_google(audio)
    except:
        saidtxt=" "
    message = saidtxt
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(message)
    print(reply)
    global text2
    text2 = font.render(reply, True, (0, 0, 0), (173, 216, 230))
    display_surface.blit(text2, (width // 2 - text2.get_width() // 2, height // 2 + 50))
    pygame.display.flip()
    engine.setProperty('voice', 'spanish')
    speak(reply)
    messages.append({"role": "assistant", "content": reply})
def chat_spanish():
    messages = [ {"role": "system", "content": 
              "I am going to use you as a translator. Google translate is bad, as its AI is not as advanced as you. I want you to take my spanish input and translate it into proper english and proper grammar. There should be no context or explanantion, just the translation"} ]

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Habla español')
            audio=r.listen(source)
            print('Hecho')
            saidtxt=r.recognize_google(audio,language="es-LA")
    except:
        saidtxt=" "
    message = saidtxt
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(message)
    print(reply)
    global text2
    text2 = font.render(reply, True, (0, 0, 0), (173, 216, 230))
    display_surface.blit(text2, (width // 2 - text2.get_width() // 2, height // 2 + 50))
    pygame.display.flip()
    engine.setProperty('voice', 'english-us')
    speak(reply)
    messages.append({"role": "assistant", "content": reply})
###################################################################################################
# Initialize Pygame
pygame.init()
# Set up window dimensions
width, height = 700, 600

# Create the window
display_surface = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("School Variety")

# Set up font and text
font = pygame.font.Font(None, 36)  # None means default font
text = font.render("School Variety", True, (0, 0, 0))  # Render text with black color

# Load images (substitute the file paths accordingly)
image1 = pygame.image.load("english.png")
image2 = pygame.image.load("spanish.png")
image3 = pygame.image.load("tour.png")
image4 = pygame.image.load("lunch.png")
image5 = pygame.image.load("school_variety.png")

# Resize images to fit the window
image1 = pygame.transform.scale(image1, (190, 50))
image2 = pygame.transform.scale(image2, (190, 50))
image3 = pygame.transform.scale(image3, (150, 115))
image4 = pygame.transform.scale(image4, (115, 115))
image5 = pygame.transform.scale(image5, (115, 115))

text2 = font.render(".", True, (0, 0, 0), (173, 216, 230))
# Game loop
while True:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and x>50 and x<240 and y>50 and y<100:
            chat_english()
        elif event.type == pygame.MOUSEBUTTONDOWN and x>450 and x<640 and y>50 and y<100:
            chat_spanish()
        elif event.type == pygame.MOUSEBUTTONDOWN and x>50 and x<200 and y>450 and y<560:
            os.system('xdg-open https://docs.google.com/presentation/d/1TQq5VOSrSNFBaLNt8m_ZsqAhhy8yWGqzaN_cVuNl5bE/edit?usp=sharing')
        elif event.type == pygame.MOUSEBUTTONDOWN and x>450 and x<560 and y>450 and y<560:
            os.system('xdg-open https://forms.gle/SyVGtpFjbfy64GUf8')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(f"Mouse Clicked at ({mouse_x}, {mouse_y})")

    # Update game logic here

    # Clear the screen
    display_surface.fill((255, 255, 255))  # Fill with white
    # Draw images on the screen (adjust positions accordingly)
    display_surface.blit(image1, (50, 50))
    display_surface.blit(image2, (450, 50))
    display_surface.blit(image3, (50, 450))
    display_surface.blit(image4, (450, 450))
    display_surface.blit(image5, (292.5, 240))
    display_surface.blit(text2, (width // 2 - text2.get_width() // 2, height // 2 + 50))
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
