import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
from time import sleep
import requests
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', help_command = None, intents=intents)
 

colorama.init()
token = input("Token: ")
headers = {
            'Authorization': token,
            'Content-Type': 'application/json'}
r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=headers)
if r.status_code == 200:
            print(f'{Fore.LIGHTGREEN_EX}Token {Fore.LIGHTRED_EX}{token}{Fore.LIGHTGREEN_EX} is valid, Logging in')
            sleep(3)
@client.event
async def on_ready():
 await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name="People Mass DM"))
 os.system('cls')
 print(f'''
{Fore.MAGENTA} ██╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
{Fore.MAGENTA}████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
{Fore.MAGENTA}██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
{Fore.MAGENTA}██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
{Fore.MAGENTA}██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
{Fore.MAGENTA}╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝
{Fore.MAGENTA}                     Logged in as {client.user.name}#{client.user.discriminator}              
{Fore.MAGENTA}                      [1] Friend Mass Dm 
{Fore.MAGENTA}                      [2] Token Checker
                                    [3] Mass Friend Deleter
                                    [4] Advanced Token Checker
                                                
''')
 sshh = input(f"{Fore.GREEN}Select: ")
 if sshh == '1':
  input2 = input(f"{Fore.GREEN}What u wanna send?: ")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} message To {user}")
 elif sshh == '2':
  headers = {
            'Authorization': token,
            'Content-Type': 'application/json'}
  r2 = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=headers)
  if r2.status_code == 200:
            print(f'{Fore.LIGHTGREEN_EX}Token {Fore.LIGHTRED_EX}{token}{Fore.LIGHTGREEN_EX} is valid, exiting in 10 seconds.')
            sleep(10)
            exit()
            
  else:
            print(f"\n{Fore.LIGHTRED_EX}Token {Fore.LIGHTGREEN_EX}{token}{Fore.LIGHTRED_EX} is invalid, exiting in 5 seconds.")
            sleep(5)
            exit()
 elif sshh == '3':
     areusure = input('Are you sure u want to delete all ur friends? (yes/no): ')
     if areusure == 'yes':
       for user in client.user.friends:
        print(f'[+] Deleted Friend {user}')
        await user.remove_friend()
        print('Deleted All Friends.')
     elif areusure == 'no':
       exit()
 elif sshh == '4':
    print(Fore.MAGENTA)
    print(f"Name = {client.user.name}")
    print(f"Username = {client.user.name}#{client.user.discriminator}")
    print(f"Email = {client.user.email}")
    print(f"Locale = {client.user.locale}")
    print(f"Flags = {client.user._flags}")
    print(f"Nitro = {client.user.premium}, {client.user.premium_type}")
    print(f"MFA = {client.user.mfa_enabled}")
    print(f"Avatar Url = {client.user.avatar_url}")
    print(f"Token = {token}")
    print(Fore.RESET)


         
          
 
 

                       

client.run(token, bot = False)
            
if r.status_code != 200:
  print(f"\n{Fore.LIGHTRED_EX}Token {Fore.LIGHTGREEN_EX}{token}{Fore.LIGHTRED_EX} is invalid, exiting in 5 seconds.")
  sleep(5)
  exit()          

     