import discord
from discord.ext import commands
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return
        
        if "$technicien" in message.content:
            variable = [
                "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide <@413456715187486730> merci de votre patience...",
                "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide <@238036776944402435> merci de votre patience...",
                "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide <@689881758375608322> merci de votre patience...",
                "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide <@272918359136272395> merci de votre patience...",
                "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide <@955522398680154153> merci de votre patience...",
                "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide <@883365972990386197> merci de votre patience...",
                "Je contact l'un de nos meilleurs techiniciens de la force d'intervention rapide <@380337408450887681> merci de votre patience...",]
            await message.reply((random.choice(variable)), mention_author=True)

        if "$ITIL" in message.content:
            await message.reply("https://discord.com/channels/955497593587245096/955497593587245099/976856914124222495", mention_author=True)

        if "$ecf" in message.content:
            await message.reply("https://cdn.discordapp.com/attachments/955497593587245099/962973316384186418/unknown.png", mention_author=True)

        if "$sharepoint" in message.content:
            await message.reply("https://campuseni.sharepoint.com/sites/CampusenLigne-Accesstagiaires", mention_author=True)

        if "$MSP2" in message.content:
            await message.reply("https://github.com/MGNXYZ/MSP2", mention_author=True)

        if "$note" in message.content:
            await message.reply("https://discord.com/channels/955497593587245096/955839740421218344/977107358310334504", mention_author=True)

        if "$ipv6" in message.content:
            await message.reply("https://iplocation.io/ipv6-compress/", mention_author=True)

        if "$mail" in message.content:
            await message.reply("https://www.hostinger.fr/tutoriels/mail-pop3-smtp-imap", mention_author=True)

        if "$regex" in message.content:
            await message.reply("https://regexr.com/", mention_author=True)

        if "$chmod" in message.content:
            await message.reply("https://linuxize.com/post/chmod-command-in-linux/", mention_author=True)

        if "$quiz" in message.content:
            await message.reply("https://quizizz.com/join/quiz/5c52c47c64ecdf001be71c73/start?studentShare=true", mention_author=True)

        if "$python" in message.content:
            await message.reply("https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=1", mention_author=True)

        if "$vlan" in message.content:
            await message.reply("https://cisco.goffinet.org/ccna/vlans/concepts-vlan-cisco/", mention_author=True)

        if "$anki" in message.content:
            await message.reply("https://discord.com/channels/955497593587245096/955839740421218344/979284159048581120", mention_author=True)

        if "$trunk" in message.content:
            await message.reply("Pas le fils de vegeta, https://formip.com/trunk/", mention_author=True)

        if "$pfsense" in message.content:
            await message.reply("https://www.provya.net/index.php?liste", mention_author=True)

        if "$masque" in message.content:
            await message.reply("https://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/", mention_author=True)

        if "$sous_reseau" in message.content:
            await message.reply("https://www.site24x7.com/fr/tools/ipv4-sous-reseau-calculatrice.html", mention_author=True)

        if "$linux" in message.content:
            await message.reply("https://www.youtube.com/playlist?list=PLrSOXFDHBtfHKxuz6NySItyf4iSEcTw97", mention_author=True)

        if "$bind" in message.content:
            await message.reply("https://arstechnica.com/gadgets/2020/08/understanding-dns-anatomy-of-a-bind-zone-file/", mention_author=True)

        if "Chika Dance" in message.content:
            await message.reply("https://cdn.discordapp.com/attachments/955497593587245099/991974360472625232/Dancin_Krono_Remix_x_Fujiwara_Chika_Dance.mp4", mention_author=True)

        if "$okidoki" in message.content:
            await message.reply("https://cdn.discordapp.com/attachments/408624206952136705/989280787805380608/Okidoki.mp4", mention_author=True)

        if "$mathieu" in message.content:
            await message.reply("https://cdn.discordapp.com/attachments/955497593587245099/991968575873097809/unknown_5.png", mention_author=True)

        if message.content.startswith("$help" or "$h"):
            embed = discord.Embed(
                title = 'Aides',
                description = ' Toute les commandes',
                color = discord.Color.red()   
            )
            embed.add_field(name= 'Commandes',value= "`$ITIL`, `$ecf`, `$MSP2`, `$note`, `$sharepoint`, `$note`, `$ipv6`, `$mail`, `$regex`, `$quiz`, `$python`, `$chmod`; `$vlan`, `$anki`, `$trunk`, `$pfsense`, `$masque`, `$sous_reseau`, `$linux`, `$bind`, `$technicien`")
            await message.reply(embed=embed)
        
client = MyClient()
client.run('OTkxOTk4NDQ2MjY3NTQzNjEy.GmAhpv.vz1wdnGdsNzi43q1dJw4O8xBPQqhL4Z7SWnxV8')
