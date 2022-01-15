import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'leave this lol', help_command = None)
 

colorama.init()
token = input("Token>> ")
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.MAGENTA} ██╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
{Fore.MAGENTA}████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
{Fore.MAGENTA}██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
{Fore.MAGENTA}██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
{Fore.MAGENTA}██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
{Fore.MAGENTA}╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝
{Fore.MAGENTA}                     By grim#5555              
{Fore.MAGENTA}                      [1] Mass Dm 
{Fore.MAGENTA}                      [2] Exit                                                 
''')
 sshh = input(f"{Fore.GREEN}Select>>")
 if sshh == '1':
  input2 = input(f"{Fore.GREEN}What Should I Send?>>")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} message To {user}")
 elif sshh == '2':
    os._exit  

client.run(token, bot = False)