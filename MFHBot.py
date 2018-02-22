# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import math
import re
import datetime
import troops

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="MFH bot Frozen Angel#9993", command_prefix="!", pm_help = False)

#Custom Functions
def twodigit(a):
    if a<10:
        return "0"+str(a)
    else:
        return str(a)

def calctime(speed, input):
    h = int(input / speed)
    rem = ((input % speed) / speed) * 60
    m = int(rem)
    s = int((rem % 1) * 60)
    return twodigit(h) + ":" + twodigit(m) + ":" + twodigit(s)+"\t\t\t\t\tArrive Time: " + str(calcArriveTime(h,m,s))


def calcArriveTime(h,m,s):
    return datetime.datetime.utcnow() + datetime.timedelta(hours=h) + datetime.timedelta(minutes=m) + datetime.timedelta(seconds=s)


# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('You are running MFHBot v0.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by FrozenAngel#9993')
	return await client.change_presence(game=discord.Game(name='Travian')) #This is buggy, let us know if it doesn't work.

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):
	await client.say(":ping_pong: Pong!")
# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.


@client.command()
async def hi(*args):
	await client.say("HOI o/")


@client.command()
async def createdby(*args):
    client.say(":warning: This bot was created by **Frozen Angel#9993**!")


@client.command()
async def hello(*args):
    await client.say("hihi o/")


@client.command()
async def time(*args):
    await client.say(" :timer: " + str(datetime.datetime.utcnow()))


@client.command()
async def distance(*args):
    pattern = re.compile("^[-]?([0-9]+)+\|[-]?([0-9]+)+$")
    if len(args) >= 2:
        if pattern.match(args[0]) and pattern.match(args[1]):
            coord1 = [int(n) for n in args[0].split('|')]
            coord2 = [int(n) for n in args[1].split('|')]
            defx = coord1[0] - coord2[0]
            defy = coord1[1] - coord2[1]
            res = math.sqrt(defx ** 2 + defy ** 2)
            if len(args) == 2:
                await client.say(" :map: Distance = " + '%.1f' % res)
            elif len(args) == 3:
                answer = ""
                answer += " :map: Distance = " + '%.1f' % res + "\n"
                tribecalls = troops.tribeidbycall(args[2])
                if len(tribecalls) != 0:
                    for tribe in tribecalls:
                        answer += " Tribe = " + str(troops.tribe(tribe)) + "\n"
                        for troop in troops.troops:
                            if troop[3] == tribe:
                                answer += "\t-> " + troop[1] + " (" + str(troop[4]) + \
                                          ")\t\t\t\t\t\t\tin: " + calctime(troop[4], res) + "\n"
                else:
                    calls = troops.idbycalltribefilter(args[2])
                    for tribe in calls:
                        if len(tribe) > 1:
                            answer += " Tribe = " + str(troops.tribename(tribe[0])) + "\n"
                            for i in range(1, len(tribe)):
                                answer += "\t-> " + troops.name(tribe[i])+" (" + str(troops.speed(tribe[i])) +\
                                          ")\t\t\t\t\t\t\tin: " + calctime(troops.speed(tribe[i]), res) + "\n"
                await client.say(answer)
    else:
        await client.say("Hey!!! tell me the coordinates!")


# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def lastdistance(*args):
    pattern = re.compile("^[-]?([0-9]+)+\|[-]?([0-9]+)+$")
    if pattern.match(args[0]) and pattern.match(args[1]):
        coord1 = [int(n) for n in args[0].split('|')]
        coord2 = [int(n) for n in args[1].split('|')]
        defx = coord1[0] - coord2[0]
        defy = coord1[1] - coord2[1]
        res = math.sqrt(defx ** 2 + defy ** 2)
        if len(args) == 2:
            await client.say(":map: Distance = " + '%.1f' % res)
        elif len(args) == 3:
            if args[2] == "Gaul" or args[2] == "G" or args[2] == "g":
                await client.say(" :map: Distance = "+ '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Phalanx (7)\t\t\t\t\t          in: " + calctime(7,res) + "\n" +
                                 "\t-> Swordsman (6)\t\t\t\t\t   in: " + calctime(6,res) + "\n" +
                                 "\t-> Pathfinder (17)\t\t\t\t\t    in: " + calctime(17,res) + "\n" +
                                 "\t-> Theutates Thunder (19)\t\tin: " + calctime(19, res) + "\n" +
                                 "\t-> Druidrider (16)\t\t\t\t\t    in: " + calctime(16, res) + "\n" +
                                 "\t-> Haeduan (13)\t\t\t\t\t       in: " + calctime(13, res) + "\n" +
                                 "\t-> Ram (4)\t\t\t\t\t\t\t        in: " + calctime(4, res) + "\n" +
                                 "\t-> Trebuchet (3)\t\t\t\t\t      in: " + calctime(3, res) + "\n" +
                                 "\t-> Chieftain (5)\t\t\t\t\t        in: " + calctime(5, res) + "\n" +
                                 "\t-> Settler (5)\t\t\t\t\t\t         in: " + calctime(5, res) + "\n")
            if args[2] == "Roman" or args[2] == "R" or args[2] == "r":
                await client.say(" :map: Distance = "+ '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Legionnaire (6)\t\t\t\t\t          in: " + calctime(6,res) + "\n" +
                                 "\t-> Praetorian (5)\t\t\t\t\t\t\t    in: " + calctime(5,res) + "\n" +
                                 "\t-> Imperian (7)\t\t\t\t\t\t\t       in: " + calctime(7,res) + "\n" +
                                 "\t-> Equites Legati (16)\t\t\t\t\t    in: " + calctime(16, res) + "\n" +
                                 "\t-> Equites Imperatoris (14)\t\t\t  in: " + calctime(14, res) + "\n" +
                                 "\t-> Equites Caesaris (10)\t\t\t\t    in: " + calctime(10, res) + "\n" +
                                 "\t-> Battering Ram (4)\t\t\t\t\t      in: " + calctime(4, res) + "\n" +
                                 "\t-> Fire Catapult (3)\t\t\t\t\t         in: " + calctime(3, res) + "\n" +
                                 "\t-> Senator (4)\t\t\t\t\t\t\t          in: " + calctime(4, res) + "\n" +
                                 "\t-> Settler (5)\t\t\t\t\t\t\t\t         in: " + calctime(5, res) + "\n")
            if args[2] == "Teuton" or args[2] == "T" or args[2] == "t":
                await client.say(" :map: Distance = "+ '%.1f' % res + "\n\nTribe: Teuton\n" +
                                 "\t-> Clubswinger (7)\t\t\t\t\t        in: " + calctime(7,res) + "\n" +
                                 "\t-> Spearman (7)\t\t\t\t\t\t\t    in: " + calctime(7,res) + "\n" +
                                 "\t-> Axeman (6)\t\t\t\t\t\t\t       in: " + calctime(6,res) + "\n" +
                                 "\t-> Scout (9)\t\t\t\t\t\t\t\t\t\tin: " + calctime(9, res) + "\n" +
                                 "\t-> Paladin (10)\t\t\t\t\t\t\t\t   in: " + calctime(10, res) + "\n" +
                                 "\t-> Teutonic Knight (9)\t\t\t\t     in: " + calctime(9, res) + "\n" +
                                 "\t-> Ram (4)\t\t\t\t\t\t\t\t\t      in: " + calctime(4, res) + "\n" +
                                 "\t-> Catapult (3)\t\t\t\t\t\t\t\t   in: " + calctime(3, res) + "\n" +
                                 "\t-> Chief (4)\t\t\t\t\t\t\t\t         in: " + calctime(4, res) + "\n" +
                                 "\t-> Settler (5)\t\t\t\t\t\t\t\t       in: " + calctime(5, res) + "\n")
            if args[2] == "Phalanx" or args[2] == "Phal" or args[2] == "phal":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Phalanx (7)\t\t\t\t\t          in: " + calctime(7, res) + "\n")
            if args[2] == "Swordsman" or args[2] == "Sword" or args[2] == "sword":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Swordsman (6)\t\t\t\t\t   in: " + calctime(6,res) + "\n")
            if args[2] == "Pathfinder":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Pathfinder (17)\t\t\t\t\t    in: " + calctime(17,res) + "\n")
            if args[2] == "Theutates Thunder" or args[2] == "TT":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Theutates Thunder (19)\t\tin: " + calctime(19, res) + "\n")
            if args[2] == "Druidrider" or args[2] == "Druid":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Druidrider (16)\t\t\t\t\t    in: " + calctime(16, res) + "\n")
            if args[2] == "Haeduan":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Haeduan (13)\t\t\t\t\t       in: " + calctime(13, res) + "\n")
            if args[2] == "Ram":
                await client.say(" :map: Distance = " + '%.1f' % res +
                                 "\n\nTribe: All\n" +
                                 "\t-> Ram/ Battering Ram (4)\t\t\t\t\t\t\t        in: " + calctime(4, res) + "\n")
            if args[2] == "Trebuchet":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Trebuchet (3)\t\t\t\t\t      in: " + calctime(3, res) + "\n")
            if args[2] == "Chieftain":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Gaul\n" +
                                 "\t-> Chieftain (5)\t\t\t\t\t        in: " + calctime(5, res) + "\n")
            if args[2] == "Settler":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: All\n" +
                                 "\t-> Settler (5)\t\t\t\t\t\t         in: " + calctime(5, res) + "\n")
            if args[2] == "Legionnaire" or args[2] == "Leg" or args[2] == "leg":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Legionnaire (6)\t\t\t\t\t          in: " + calctime(6,res) + "\n")
            if args[2] == "Praetorian" or args[2] == "Pret" or args[2] == "pret":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Praetorian (5)\t\t\t\t\t\t\t    in: " + calctime(5,res) + "\n")
            if args[2] == "Imperian" or args[2] == "Imp":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Imperian (7)\t\t\t\t\t\t\t       in: " + calctime(7,res) + "\n")
            if args[2] == "Equites Legati" or args[2] == "Legati":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Equites Legati (16)\t\t\t\t\t    in: " + calctime(16, res) + "\n")
            if args[2] == "Equites Imperatoris" or args[2] == "EI":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Equites Imperatoris (14)\t\t\t  in: " + calctime(14, res) + "\n")
            if args[2] == "Equites Caesaris" or args[2] == "EC":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Equites Caesaris (10)\t\t\t\t    in: " + calctime(10, res) + "\n")
            if args[2] == "Battering Ram":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Battering Ram (4)\t\t\t\t\t      in: " + calctime(4, res) + "\n")
            if args[2] == "Fire Catapult":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Fire Catapult (3)\t\t\t\t\t         in: " + calctime(3, res) + "\n")
            if args[2] == "Senator":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Roman\n" +
                                 "\t-> Senator (4)\t\t\t\t\t\t\t          in: " + calctime(4, res) + "\n")
            if args[2] == "Clubswinger" or args[2] == "Clubs" or args[2] == "clubs":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Teuton\n" +
                                 "\t-> Clubswinger (7)\t\t\t\t\t        in: " + calctime(7,res) + "\n")
            if args[2] == "Spearman" or args[2] == "Spear" or args[2] == "spear":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Teuton\n" +
                                 "\t-> Spearman (7)\t\t\t\t\t\t\t    in: " + calctime(7,res) + "\n")
            if args[2] == "Axeman" or args[2] == "Axe" or args[2] == "axe":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Teuton\n" +
                                 "\t-> Axeman (6)\t\t\t\t\t\t\t       in: " + calctime(6,res) + "\n")
            if args[2] == "Scout":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Teuton\n" +
                                 "\t-> Scout (9)\t\t\t\t\t\t\t\t\t\tin: " + calctime(9, res) + "\n")
            if args[2] == "Paladin":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Teuton\n" +
                                 "\t-> Paladin (10)\t\t\t\t\t\t\t\t   in: " + calctime(10, res) + "\n")
            if args[2] == "Teutonic Knight" or args[2] == "TK":
                await client.say(" :map: Distance = " + '%.1f' % res + "\n\nTribe: Teuton\n" +
                                 "\t-> Teutonic Knight (9)\t\t\t\t     in: " + calctime(9, res) + "\n")
            if args[2] == "Catapult" or args[2] == "Cat" or args[2] == "cat":
                await client.say(" :map: Distance = " + '%.1f' % res +
                                 "\n\nTribe: All\n" +
                                 "\t-> Fire Catapult/ Trebuchet/ Catapult (3)\t\t\t\t\t in: " + calctime(3, res) + "\n")
            if args[2] == "Chief":
                await client.say(" :map: Distance = " + '%.1f' % res +
                                 "\n\nTribe: Roman/ Teuton\n" +
                                 "\t-> Senator/ Chief (4)\t\t\t\t\t\t\t          in: " + calctime(4, res) + "\n" +
                                 "\n\nTribe: Gaul\n" +
                                 "\t-> Chieftain (5)\t\t\t\t\t        in: " + calctime(5, res) + "\n")
    else:
        await client.say(":warning: Invalid coordination, use number|number format.")


@client.command()
async def oasisres(*args):
    time = int(args[1])/60
    if args[0] == "25l":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*40)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*11)))
    if args[0] == "25l-25w" or args[0] == "25w-25l":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*40)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*41)))
    if args[0] == "50l":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*80)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*11)))
    if args[0] == "25c":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*40)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*11)))
    if args[0] == "25c-25w" or args[0] == "25w-25c":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*40)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*41)))
    if args[0] == "50c":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*80)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*11)))
    if args[0] == "25i":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*40)) + ", Crop = " + str(int(time*11)))
    if args[0] == "25i-25w" or args[0] == "25w-25i":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*40)) + ", Crop = " + str(int(time*41)))
    if args[0] == "50i":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*80)) + ", Crop = " + str(int(time*11)))
    if args[0] == "50w":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*81)))
    if args[0] == "25w":
        await client.say(" :deciduous_tree: Lumber = " + str(int(time*10)) + ", Clay = " + str(int(time*10)) + ", Iron = " + str(int(time*10)) + ", Crop = " + str(int(time*41)))

@client.command()
async def function(*args):
    if len(args)==0:
        await client.say("You can see all of my functions if you type !functions.\nYou can see help for the functions if you type !function [Function Name].\n TY for using me! I'll be cute :)")
    else :
        if args[0] == "distance":
            await client.say("Calculates the distance between map tiles.\n" +
                             "\t\tThis function can calculate the travel time and arrive time of different troop types.\n" +
                             "*!distance [Coord1] [Coord2] [Tribe/Troop Name (Optional)]*\n\n\n" +
                             "Coordinates must be in x|y format.\n"
                             "**Tribes:** Gaul/G/g - Roman/R/r - Teuton/T/t\n"
                             "**Gaul Troops:**\n" +
                             "\tPhalanx/Phal/phal, Swordsman/Sword/sword, Pathfinder, Theutates Thunder/TT, Druidrider/Druid, Haeduan, Ram, Trebuchet, Chieftain, Settler\n" +
                             "**Roman Troops:**\n" +
                             "\tLegionnaire/Leg/leg, Praetorian/Pret/pret, Imperian/Imp/imp, Equites Legati/EL, Equites Imperatoris/EI, Equites Caesaris/EC, Battering Ram, Fire Catapult, Senator, Settler\n" +
                             "**Teuton Troops:**\n" +
                             "\tClubswinger/Clubs/clubs, Spearman/Spear/spear, Axeman/Axe/axe, Scout, Paladin, Teutonic Knight/TK, Ram, Catapult/Cat/cat, Chief, Settler\n")
        elif args[0] == "time":
            await client.say("Returns server time.")
        elif args[0] == "oasisres":
            await client.say("Calculates the respawned resources in the oasis.\n" +
                             "*!oasisres [Oasis Type] [Time]*\n\n\n" +
                             "**Oasis Types:**\n" +
                             "\t25l: 25% Lumber\n" +
                             "\t25l-25w/25w-25l: 25% Lumber & 25% Crop\n" +
                             "\t50l: 50% Lumber\n" +
                             "\t25c: 25% Clay\n" +
                             "\t25c-25w/25w-25c: 25% Clay & 25% Crop\n" +
                             "\t50c: 50% Clay\n" +
                             "\t25i: 25% Iron\n" +
                             "\t25i-25w/25w-25i: 25% Iron & 25% Crop\n" +
                             "\t50c: 50% Iron\n" +
                             "\t50w: 50% Crop\n" +
                             "\t25w: 25% Crop\n")

@client.command()
async def functions(*args):
    await client.say("!time: Returns server time.\n" +
                     "!distance [Coord1] [Coord2] [Tribe/Troop Name (Optional)]: Calculates the distance between map tiles.\n" +
                     "\t\tThis function can calculate the travel time and arrive time of different troop types.\n" +
                     "!oasisres [Oasis Type] [Time]: Calculates the respawned resources in the oasis.\n")

# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.
	
client.run('NDE1NTAxNzE4NTA4NDA0NzQ3.DW23yg.AfG3caU1E2Y8Qk4a-vNHS0gOMxA')

# Basic Bot was created by Frozen Angel#9993

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.