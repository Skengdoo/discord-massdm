import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('niggers')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('Nzg0OTY4NTQ1OTI2Nzc0Nzg3.YPtCIQ.I1_EAvhTf9PoLA7ylN8BL2hDwns', bot=False)
