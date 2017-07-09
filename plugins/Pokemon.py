import slackbot.bot
import random
Mname = "Minion"
Mlv = 5
Mhp = Mlv*5
Matk = Mlv
Magi = Mlv
Mexp = 0
Mshape="""\
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

Mmonster = {'Mname':Mname, 'Mlv':Mlv, 'Mhp':Mhp, 'Matk':Matk, 'Magi':Magi, 'Mexp':Mexp , 'Mshape':Mshape}
monster = None
inbattle = False

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
    global monster

    # sub hp

    hurt = Mmonster['Matk'] + random.randint(0,Mmonster['Mlv'])
    if random.randint(1,100-(monster['agi']-Mmonster['Magi']))>=95:
        hurt = 0
    monster['hp'] -= hurt
    if monster['hp'] <= 0:
        Mmonster['Mexp'] += monster['exp']
        reply = '{name:s} becomes unconscious status.\nYour {Mname:s} got {exp:d} EXP.\n'.format(**monster,**Mmonster)
        if Mmonster['Mexp']>=Mmonster['Mlv']*5:
            Mmonster['Mexp']=Mmonster['Mexp']-5
            Mmonster['Mlv']= Mmonster['Mlv']+1
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
            reply = '{name:s} got {hurt:d} hurts (HP:{hp:d}).\nYour {Mname:s} got {Mhurt:d} hurts (HP:{Mhp:d}) and becomes unconscious status.\n'.format(**monster, **Mmonster, hurt=hurt, Mhurt=Mhurt)
            monster = None
            inbattle = False
        else:
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
    global inbattle

    if not inbattle:
        Mmonster['Mhp'] = Mmonster['Mlv']*5
        reply = 'Your pokemons are all recovered.'
    else: reply = 'You are still in a battle.'
    message.reply(reply)
@slackbot.bot.respond_to(r'^Catch')
def resp_fizzbuzz(message):

    global context
    global monster
    global Mmonster
    global inbattle

    if inbattle:
        Mmonster['Mname'] = monster['name']
        Mmonster['Mlv'] = monster['lv']
        Mmonster['Mhp'] = monster['hp']
        Mmonster['Matk'] = monster['atk']
        Mmonster['Magi'] = monster['agi']
        Mmonster['Mshape'] = monster['shape']
        reply = 'Your pokemon has been changed.'
        inbattle = False
    else: reply = 'There is no Pokemon.'
    message.reply(reply)

@slackbot.bot.respond_to(r'^Pokemonstatus')
def resp_fizzbuzz(message):

    global context
    global monster
    global Mmonster
    global inbattle

    if not inbattle:
        reply = '{Mshape:s}\nPOKEMON:{Mname:s}\nLEVEL:{Mlv:d}\nHP:{Mhp:d}\nATK:{Matk:d}\nAGI:{Magi:d}\nEXP:{Mexp:d}\n.'.format(**Mmonster)
    else: reply = 'You are still in a battle.'
    message.reply(reply)
