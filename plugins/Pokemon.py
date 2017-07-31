import slackbot.bot
import random
Pokemonindex = 1
Mname1 = "Minion"
Mlv1 = 5
Mhp1 = Mlv1*5
Matk1 = Mlv1
Magi1 = Mlv1
Mexp1 = 0
Mshape1="""\
───────────▄▄▄█▄▄█▄▄█▄▄▄
────────▄▀▀═════════════▀▀▄
───────█═══════════════════█
──────█═════════════════════█
─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
────█═══█████████═█████████═══█
────█══██▀────▀█████▀────▀██══█
───██████──█▀█──███──█▀█──██████
───██████──▀▀▀──███──▀▀▀──██████
────█══▀█▄────▄██─██▄────▄█▀══█
────█════▀█████▀───▀█████▀════█
────█═════════════════════════█
────█═════════════════════════█
────█═══════▀▄▄▄▄▄▄▄▄▄▀═══════█
────█═════════════════════════█
───▐▓▓▌═════════════════════▐▓▓▌
"""
Mname2 = ''
Mlv2 = -1
Mhp2 = -1
Matk2 = -1
Magi2 = -1
Mexp2 = -1
Mshape2 = ''
Mname3 = ''
Mlv3 = -1
Mhp3 = -1
Matk3 = -1
Magi3 = -1
Mexp3 = -1
Mshape3 = ''
Mname4 = ''
Mlv4 = -1
Mhp4 = -1
Matk4 = -1
Magi4 = -1
Mexp4 = -1
Mshape4 = ''
Mname5 = ''
Mlv5 = -1
Mhp5 = -1
Matk5 = -1
Magi5 = -1
Mexp5 = -1
Mshape5 = ''
Mname6 = ''
Mlv6 = -1
Mhp6 = -1
Matk6 = -1
Magi6 = -1
Mexp6 = -1
Mshape6 = ''
Mmonster1  = {'Mname':Mname1, 'Mlv':Mlv1, 'Mhp':Mhp1, 'Matk':Matk1, 'Magi':Magi1, 'Mexp':Mexp1 , 'Mshape':Mshape1}
Mmonster2  = {'Mname':Mname2, 'Mlv':Mlv2, 'Mhp':Mhp2, 'Matk':Matk2, 'Magi':Magi2, 'Mexp':Mexp2 , 'Mshape':Mshape2}
Mmonster3 = {'Mname':Mname3, 'Mlv':Mlv3, 'Mhp':Mhp3, 'Matk':Matk3, 'Magi':Magi3, 'Mexp':Mexp3 , 'Mshape':Mshape3}
Mmonster4  = {'Mname':Mname4, 'Mlv':Mlv4, 'Mhp':Mhp4, 'Matk':Matk4, 'Magi':Magi4, 'Mexp':Mexp4 , 'Mshape':Mshape4}
Mmonster5 = {'Mname':Mname5, 'Mlv':Mlv5, 'Mhp':Mhp5, 'Matk':Matk5, 'Magi':Magi5, 'Mexp':Mexp5 , 'Mshape':Mshape5}
Mmonster6  = {'Mname':Mname6, 'Mlv':Mlv6, 'Mhp':Mhp6, 'Matk':Matk6, 'Magi':Magi6, 'Mexp':Mexp6 , 'Mshape':Mshape6}
SixPokemons = {1:Mmonster1,2:Mmonster2,3:Mmonster3,4:Mmonster4,5:Mmonster5,6:Mmonster6}

Mmonster = SixPokemons[Pokemonindex]

monster = None
inbattle = False
instatus = False

def notinbattle_action():
    global inbattle
    global Mmonster
    global monster
    # initialize monster
    name = "Pikachu"
    if Mmonster['Mlv']>=5:
        lv = Mmonster['Mlv'] -5 + random.randint(0,10)
    else :
        lv = Mmonster['Mlv']
    hp = lv*4+random.randint(0,lv)
    atk = lv
    agi = lv
    exp = lv
    shape="""\
░░░░█░▀▄░░░░░░░░░░▄▄███▀
░░░░█░░░▀▄░▄▄▄▄▄░▄▀░░░█▀
░░░░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░░░░▌░▄▄░░░▄▄░▐▀▀
░░░░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
░░░▄▀▀▐▀▀░░░░░░░▀▀▌▄▄▄░░░█
░░░█░░░▀▄░░░░░░░▄▀░░░░█▀▀▀
░░░░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
"""

    monster1 = {'name':name, 'lv':lv, 'hp':hp, 'atk':atk, 'agi':agi, 'exp':exp , 'shape':shape}

    name = "Duck"
    if Mmonster['Mlv']>=5:
        lv = Mmonster['Mlv'] -5 + random.randint(0,10)
    else :
        lv = Mmonster['Mlv']
    hp = lv*4+random.randint(0,lv)
    atk = lv
    agi = lv
    exp = lv
    shape="""\
    　　　　　　　　▓▓▓▓▓▓
　　　██　　　▓▒▒▒▒▒▓
　　　　███..▓░░░▒▒▒▒▓
　　　　████░▒▒░░▒▒▒▓
　　　　　███░▒(O)▒░▒▒▓
        ~ ██░░░░░▒▒▒▓
　　　　　███▒░░░▒▒▒▒▓
　　　　███..▓▒▒▒▒▒▒▓
　　　██　　　▓▒▒▒▒▓
　　　　　　　▓▒▒▒▓
　　　　　　.▓▒▒▒▒▓
"""

    monster2 = {'name':name, 'lv':lv, 'hp':hp, 'atk':atk, 'agi':agi, 'exp':exp , 'shape':shape}

    name = "Weney"
    if Mmonster['Mlv']>=5:
        lv = Mmonster['Mlv'] -5 + random.randint(0,10)
    else :
        lv = Mmonster['Mlv']
    hp = lv*4+random.randint(0,lv)
    atk = lv
    agi = lv
    exp = lv
    shape="""\
    ┴┬┴┬／￣＼＿／￣＼
┬┴┬┴▏　　▏▔▔▔▔＼
┴┬┴／＼　／　　　　　　﹨
┬┴∕　　　　　　　／　　　） ╮╰╮ ╭ ╯╭╰╮
┴┬▏　　　　　　　　●　　▏ ╮╰╮ ╭ ╯╭╰╮
┬┴▏　　　　　　　　　　　▔█ ◥█□█□█□█◤
┴◢██◣　　　　　　 ＼＿＿／ 　█○●○●○█
┬█████◣　　　　　　／　　 　█○●○●○█
┴████████████◣ 　　◥█□█□█◤　
◢████████████▆▄ 　　▆███▆
"""

    monster3 = {'name':name, 'lv':lv, 'hp':hp, 'atk':atk, 'agi':agi, 'exp':exp , 'shape':shape}

    name = "Jacket"
    if Mmonster['Mlv']>=5:
        lv = Mmonster['Mlv'] -5 + random.randint(0,10)
    else :
        lv = Mmonster['Mlv']
    hp = lv*4+random.randint(0,lv)
    atk = lv
    agi = lv
    exp = lv
    shape="""\
..........................╱......╲=========== = ╱　 ╲....................
　　　　　╱╲　　　╲　　　　╱　　　╱╲
　　　　╱　　╲　　╱╲⊙︳╱╲　　╱　　╲
　　　╱　　　　╲╱　╱　︳╲　╲╱　　　　╲
　　╱　　　　　　╲╱　　︳　╲╱　　　　　　╲
　╱╲　　╱▏　　　　　　︳　　　　　▕╲　　╱╲
　╲　╲╱　▏　　　　　⊙︳　　　　　▕　╲╱　╱
　　╲╱　　▏　　　　　　︳　　　　　▕　　╲╱
　　　　　　▏　╴╴　　　︳　╴╴　　▕
　　　　　　▏　▏　▏　　︳　▏　▏　▕
　　　　　　▏　▏　▏　⊙︳　▏　▏　▕
　　　　　　▏　￣￣　　　︳　￣￣　　▕
　　　　　　￣￣￣￣￣￣￣￣￣￣￣￣￣￣
"""

    monster4 = {'name':name, 'lv':lv, 'hp':hp, 'atk':atk, 'agi':agi, 'exp':exp , 'shape':shape}
    name = "Minion"
    if Mmonster['Mlv']>=5:
        lv = Mmonster['Mlv'] -5 + random.randint(0,10)
    else :
        lv = Mmonster['Mlv']
    hp = lv*4+random.randint(0,lv)
    atk = lv
    agi = lv
    exp = lv
    shape="""\
───────────▄▄▄█▄▄█▄▄█▄▄▄
────────▄▀▀═════════════▀▀▄
───────█═══════════════════█
──────█═════════════════════█
─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
────█═══█████████═█████████═══█
────█══██▀────▀█████▀────▀██══█
───██████──█▀█──███──█▀█──██████
───██████──▀▀▀──███──▀▀▀──██████
────█══▀█▄────▄██─██▄────▄█▀══█
────█════▀█████▀───▀█████▀════█
────█═════════════════════════█
────█═════════════════════════█
────█═══════▀▄▄▄▄▄▄▄▄▄▀═══════█
────█═════════════════════════█
───▐▓▓▌═════════════════════▐▓▓▌
"""

    monster5 = {'name':name, 'lv':lv, 'hp':hp, 'atk':atk, 'agi':agi, 'exp':exp , 'shape':shape}

    monseterlist ={1:monster1,2:monster2,3:monster3,4:monster4,5:monster5}

    monster = monseterlist[random.randint(1,5)]
        ##reply = "{name:s} is ... HP:{hp:d}".format(name=name, hp=hp)
    reply = "Pops up!!\nLevel {lv:d} {name:s} [HP:{hp:d}]\n{shape:s}\n".format(**monster)


    inbattle = True

    return reply

def inbattle_action():
    global inbattle
    global Mmonster

    global Pokemonindex
    global SixPokemons
    global monster

    # sub hp

    hurt = Mmonster['Matk'] + random.randint(0,Mmonster['Mlv'])
    if random.randint(1,100-(monster['agi']-Mmonster['Magi']))>=95:
        hurt = 0
    monster['hp'] -= hurt
    if monster['hp'] <= 0:
        Mmonster['Mexp'] += monster['exp']
        SixPokemons[Pokemonindex] = Mmonster
        reply = '{name:s} becomes unconscious status.\nYour {Mname:s} got {exp:d} EXP.\n'.format(**monster,**Mmonster)
        if Mmonster['Mexp']>=Mmonster['Mlv']*5:
            Mmonster['Mexp']=Mmonster['Mexp']-5
            Mmonster['Mlv']= Mmonster['Mlv']+1
            SixPokemons[Pokemonindex] = Mmonster
            reply = reply+'Congratulation!! Your {Mname:s} is level up.[LV.{Mlv:d}]'.format(**Mmonster)
            monster = None
            inbattle = False
        else:
            monster = None
            inbattle = False
    else:
        Mhurt = monster['atk'] + random.randint(0,monster['lv'])
        if random.randint(1,100-(Mmonster['Magi']-monster['agi']))>=95:
            Mhurt = 0
        Mmonster['Mhp'] -= Mhurt
        if Mmonster['Mhp'] <= 0:
            SixPokemons[Pokemonindex] = Mmonster
            reply = '{name:s} got {hurt:d} hurts (HP:{hp:d}).\nYour {Mname:s} got {Mhurt:d} hurts (HP:{Mhp:d}) and becomes unconscious status.\n'.format(**monster, **Mmonster, hurt=hurt, Mhurt=Mhurt)
            monster = None
            inbattle = False
        else:
            SixPokemons[Pokemonindex] = Mmonster
            reply = '{name:s} got {hurt:d} hurts (HP:{hp:d}).\nYour {Mname:s} got {Mhurt:d} hurts (HP:{Mhp:d}).\n[Fight or Escape or Catch ?]'.format(**monster, **Mmonster, hurt=hurt, Mhurt=Mhurt)

    return reply

@slackbot.bot.respond_to(r'^Battle')
def resp_fizzbuzz(message):

    global context
    global inbattle
    global monster
    global Mmonster
    if not inbattle:
        if Mmonster['Mhp']>0:
            reply = notinbattle_action() + 'Your Level {Mlv:d} {Mname:s} [HP:{Mhp:d}]\n{Mshape:s}\n[Fight or Escape or Catch ?]'.format(**monster,**Mmonster)
        else: reply = 'Your {Mname:s} is still unconscious.'.format(**Mmonster)
    else: reply = 'You are still in a battle.\nLevel {lv:d} {name:s} [HP:{hp:d}]\n{shape:s}\nYour Level {Mlv:d} {Mname:s} [HP:{Mhp:d}]\n{Mshape:s}\n[Fight or Escape or Catch ?]'.format(**monster,**Mmonster)
    message.reply(reply)

@slackbot.bot.respond_to(r'^Fight')
def resp_fizzbuzz(message):

    global context
    global monster
    global Mmonster
    global inbattle

    if inbattle:
        reply = inbattle_action()
    else: reply = 'You are not in a battle.'
    message.reply(reply)

@slackbot.bot.respond_to(r'^Escape')
def resp_fizzbuzz(message):

    global context
    global inbattle

    if inbattle:
        inbattle = False
        reply = 'You escape from the battle with {name:s}.'.format(**monster)
    else: reply = 'You are not in a battle.'

    message.reply(reply)

@slackbot.bot.respond_to(r'^Pokemoncenter')
def resp_fizzbuzz(message):

    global context
    global monster
    global Mmonster

    global Pokemonindex
    global SixPokemons
    global inbattle

    if not inbattle:
        for i in range(1, 7, +1):
            if SixPokemons[i]['Mlv'] != -1 :
                SixPokemons[i]['Mhp'] = SixPokemons[i]['Mlv']*5
        Mmonster = SixPokemons[Pokemonindex]
        reply = 'Your pokemons are all recovered.'
    else: reply = 'You are still in a battle.'
    message.reply(reply)
@slackbot.bot.respond_to(r'^Catch')
def resp_fizzbuzz(message):

    global context
    global monster
    global Mmonster
    global Pokemonindext
    global SixPokemons
    global inbattle

    if inbattle:

        loading = 0
        for i in range(1, 7, +1):
            if SixPokemons[i]['Mlv'] != -1 :
                loading = loading+1
        if loading<6 :
            if random.randint(0,monster['lv'])*5>monster['hp']:
                for i in range(1, 7, +1):
                    if SixPokemons[i]['Mlv'] == -1 :
                        SixPokemons[i]['Mname'] = monster['name']
                        SixPokemons[i]['Mlv'] = monster['lv']
                        SixPokemons[i]['Mhp'] = monster['hp']
                        SixPokemons[i]['Matk'] = monster['atk']
                        SixPokemons[i]['Magi'] = monster['agi']
                        SixPokemons[i]['Mshape'] = monster['shape']
                        SixPokemons[i]['Mexp'] = 0
                        break
                SixPokemons[Pokemonindex] = Mmonster
                reply = 'You catched the pokemon.'
                inbattle = False
            else:
                Mhurt = monster['atk'] + random.randint(0,monster['lv'])
                if random.randint(1,100-(Mmonster['Magi']-monster['agi']))>=95:
                    Mhurt = 0
                Mmonster['Mhp'] -= Mhurt
                if Mmonster['Mhp'] <= 0:
                    SixPokemons[Pokemonindex] = Mmonster
                    reply = 'You failed in catching the pokemon (HP:{hp:d}).\nYour {Mname:s} got {Mhurt:d} hurts (HP:{Mhp:d}) and becomes unconscious status.\n'.format(**monster,**Mmonster, Mhurt=Mhurt)
                    monster = None
                    inbattle = False
                else:
                    SixPokemons[Pokemonindex] = Mmonster
                    reply = 'You failed in catching the pokemon (HP:{hp:d}).\nYour {Mname:s} got {Mhurt:d} hurts (HP:{Mhp:d}).\n[Fight or Escape or Catch ?]'.format(**monster,**Mmonster, Mhurt=Mhurt)

        else: reply = 'Your Pocket is full.'
    else: reply = 'There is no Pokemon.'
    message.reply(reply)

@slackbot.bot.respond_to(r'^Pokemonstatus')
def resp_fizzbuzz(message):
    global Pokemonindex
    global context
    global monster
    global Mmonster
    global SixPokemons
    global inbattle
    global instatus
    if not inbattle:
        instatus = True
        reply = ''
        for i in range(1, 7, +1):
            if SixPokemons[i]['Mlv'] != -1 :
                reply = reply + '******No.'+str(i)+'******\n'+'{Mshape:s}\nPOKEMON:{Mname:s}\nLEVEL:{Mlv:d}\nHP:{Mhp:d}\nATK:{Matk:d}\nAGI:{Magi:d}\nEXP:{Mexp:d}\n[Shift to ?(Shift + (1~6))]\n'.format(**SixPokemons[i])
    else: reply = 'You are still in a battle.'
    message.reply(reply)

    @slackbot.bot.respond_to(r'^Shift\s+(\d+)')
    def resp_fizzbuzz(message, digitstr):
        global instatus
        global Pokemonindex
        global context
        global monster
        global Mmonster
        global SixPokemons
        global inbattle
        if instatus:
            Pokemonindex = int(digitstr)
            Mmonster = SixPokemons[Pokemonindex]
            instatus = False
            reply = 'Your fighting Pokemon has shifted to {Mname:s}.\n.'.format(**SixPokemons[Pokemonindex])
            message.reply(reply)
        else:
            reply = 'You are not in a Pokemonstatus.'
            message.reply(reply)
