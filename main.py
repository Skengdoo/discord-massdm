import discord, json, os, requests, colorama, re, time, threading, sys, ctypes
from colorama import Fore
colorama.init()
client = discord.Client()

if sys.platform.startswith("win"):
    ctypes.windll.kernel32.SetConsoleTitleW(f"skengdoo sexy message all friends tool")
else:
    pass

with open('config.json') as w:
    config = json.load(w)

token = config.get('token')
def initiate():
    try:
        client.run(token, bot=False)
    except discord.errors.LoginFailure:
        print(f"{Fore.GREEN} > {Fore.RED}INCORRECT TOKEN VALUE PARSED" + Fore.RESET)
        time.sleep(3)
        exit()
       
def exit():
    os._exit(2)

def clear():
    os.system('cls')


def ui():
    print(f'''{Fore.RESET}
                            ╦══╗ ╔═╦═╗ ╔══╗ ╦    ╦ 
                            ║  ║ ║ ║ ║ ╠══╣ ║    ║
                            {Fore.RED}╩══╝ ╩   ╩ ╩  ╩ ╩══╝ ╩══╝{Fore.RESET}
                            {Fore.GREEN} skengdoo {Fore.RESET}
                        ────────────────────────────────    
                    
''')


async def menu():
    ui()
    print(f"{Fore.RESET}Message For Noobs {Fore.GREEN}>{Fore.RESET} ", end=''); message = str(input(''))
    print("")
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"{Fore.GREEN} > {Fore.RESET}Sent DM To: {user.name}")
        except:
            print(f"{Fore.GREEN} > {Fore.RESET}Couldn't Send DM To: {user.name}")
    print(f"{Fore.GREEN} > {Fore.RESET}Completed!")



@client.event
async def on_connect():
    clear()
    await menu()


if __name__ == '__main__':
    initiate()
