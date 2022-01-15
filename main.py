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
{Fore.MAGENTA}                     Logged in as {client.user.name}#{client.user.discriminator}              
{Fore.MAGENTA}                      [1] Mass Dm 
{Fore.MAGENTA}                      [2] Suprise                                                 
''')
 sshh = input(f"{Fore.GREEN}Select>>")
 if sshh == '1':
  input2 = input(f"{Fore.GREEN}What u wanna send?>>")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} message To {user}")
 elif sshh == '2':
    print(f'{Fore.MAGENTA}\nwhat did u expect lol')
    os._exit  

client.run(token, bot = False)
