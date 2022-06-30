from pydoc import cli
import discord, asyncio
from discord.ext import commands
import random

class MyClient(discord.Client):  

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        minTime = 43200 #minimum time in seconds
        maxTime = 72800 #maximum time in seconds
        channel = self.get_channel(955497593587245099)
        msgFx = [
            "C'est la pause",
            "On reprend",
            "C'est l'heure de manger",
            "On fait un pause",
            "Bonne soirée à tous ! A demain !",
            "Faites une pause",
            "C'est la pause déj",
            "On reprend =)",
            "C'est fini pour aujourd'hui"
        ]
        embed = discord.Embed(
                title = "__Message d'utilité générale de la part de FX:__",
                description = "",
                color = discord.Color.purple()   
            )
        while True:
            embed.description = "`" + random.choice(msgFx) + "`" 
            await asyncio.sleep(random.randint(minTime, maxTime))
            await channel.send(embed=embed)

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        dictionnaireMessageSimple = {
            "$ITIL"         : "https://discord.com/channels/955497593587245096/955497593587245099/976856914124222495",
            "$ecf"          : "https://cdn.discordapp.com/attachments/955497593587245099/962973316384186418/unknown.png",
            "$sharepoint"   : "https://campuseni.sharepoint.com/sites/CampusenLigne-Accesstagiaires", 
            "$MSP2"         : "https://github.com/MGNXYZ/MSP2",
            "$note"         : "https://discord.com/channels/955497593587245096/955839740421218344/977107358310334504", 
            "$ipv6"         : "https://iplocation.io/ipv6-compress/", 
            "$mail"         : "https://www.hostinger.fr/tutoriels/mail-pop3-smtp-imap",
            "$regex"        : "https://regexr.com/",
            "$chmod"        : "https://linuxize.com/post/chmod-command-in-linux/",
            "$quiz"         : "https://quizizz.com/join/quiz/5c52c47c64ecdf001be71c73/start?studentShare=true",
            "$python"       : "https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=1",
            "$vlan"         : "https://cisco.goffinet.org/ccna/vlans/concepts-vlan-cisco/",
            "$anki"         : "https://discord.com/channels/955497593587245096/955839740421218344/979284159048581120",
            "$trunk"        : "Pas le fils de vegeta, https://formip.com/trunk/",
            "$pfsense"      : "https://www.provya.net/index.php?liste",
            "$masque"       : "https://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/",
            "$sous_reseau"  : "https://www.site24x7.com/fr/tools/ipv4-sous-reseau-calculatrice.html",
            "$linux"        : "https://www.youtube.com/playlist?list=PLrSOXFDHBtfHKxuz6NySItyf4iSEcTw97",
            "$bind"         : "https://arstechnica.com/gadgets/2020/08/understanding-dns-anatomy-of-a-bind-zone-file/",
            "Chika Dance"   : "https://cdn.discordapp.com/attachments/955497593587245099/991974360472625232/Dancin_Krono_Remix_x_Fujiwara_Chika_Dance.mp4",
            "$okidoki"      : "https://cdn.discordapp.com/attachments/408624206952136705/989280787805380608/Okidoki.mp4",
            "$mathieu"      : "https://cdn.discordapp.com/attachments/955497593587245099/991968575873097809/unknown_5.png"
        }
        
        for motCle in dictionnaireMessageSimple:
            if motCle in message.content:
                await self.envoyerReponse(message, dictionnaireMessageSimple[motCle])

        if "$technicien" in message.content:
            mentionTechnicien = [
                "<@413456715187486730>", # 
                "<@238036776944402435>", #
                "<@689881758375608322>", #
                "<@272918359136272395>", #  ça serait pas mal de mettre en commentaire les gens à qui ça correspond, histoire de pas avoir à chercher
                "<@955522398680154153>", #
                "<@883365972990386197>", #
                "<@380337408450887681>"  #
            ]
            appelTechnicien = "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide " + random.choice(mentionTechnicien) +  " merci de votre patience..."
            await self.envoyerReponse(message, appelTechnicien)

        if message.content.startswith("$help" or "$h"):
            embed = discord.Embed(
                title = 'Aides',
                description = ' Toute les commandes',
                color = discord.Color.red()   
            )
            embed.add_field(name= 'Commandes',value= "`$ITIL`, `$ecf`, `$MSP2`, `$note`, `$sharepoint`, `$note`, `$ipv6`, `$mail`, `$regex`, `$quiz`, `$python`, `$chmod`; `$vlan`, `$anki`, `$trunk`, `$pfsense`, `$masque`, `$sous_reseau`, `$linux`, `$bind`, `$technicien`")
            await message.reply(embed=embed)

    async def envoyerReponse(self, message, contenu):
        await message.reply(contenu, mention_author=True) 

client = MyClient()
client.run('TOKEN')
