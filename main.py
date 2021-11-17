import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


API_KEY = '1979627419:AAEJabO6yrQBE6bWKAsTw5YcfWBJdNX83e4'

bot = telebot.TeleBot(API_KEY)


user = {}
user_list = []

#####################################################################
#Start game
@bot.message_handler(commands=['start'])
def intro(message):
  msg = bot.send_message(message.chat.id, "Enter first name.")

  bot.register_next_step_handler(msg, process_name1)

def process_name1(message):
  name = message.text
  user[name] = 0
  user_list.append(name)
  msg = bot.send_message(message.chat.id, "Enter second name.")

  bot.register_next_step_handler(msg, process_name2)
  

def process_name2(message):
  name = message.text
  user[name] = 0
  user_list.append(name)
  msg = bot.send_message(message.chat.id, "Enter third name.")

  bot.register_next_step_handler(msg, process_name3)

def process_name3(message):
  name = message.text
  user[name] = 0
  user_list.append(name)
  msg = bot.send_message(message.chat.id, "Enter forth name.")

  bot.register_next_step_handler(msg, process_name4)

def process_name4(message):
  name = message.text
  user[name] = 0
  user_list.append(name)
  msg = bot.send_message(message.chat.id, "Enter bet.")
  bot.register_next_step_handler(msg, process_bet)

def process_bet(message):
  global bet
  bet = float(message.text)
  #print(message)
  #msg = bot.send_message(message.chat.id, "OK to start game")
  #id = message.chat.id
  #chat_id = message.json['chat']['id']
  #bot.register_next_step_handler(msg, display_score)
  display_score(message)

def display_score(message):
  response = ""
  for name, amount in user.items():
    response += (name + " : " + str(amount)+ "  |  ")
  response = response + "\n" + "BET: " + str(bet)
  return bot.send_message(message.chat.id, response, reply_markup = markup_inline())

############################################################
#Inlinekeyboard
def markup_inline():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton("湖", callback_data="win"),
    InlineKeyboardButton("杠", callback_data="kong"),
    InlineKeyboardButton("咬", callback_data="bite")
  )

  return markup

def markup_inline_win():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton(user_list[0], callback_data=user_list[0]),
    InlineKeyboardButton(user_list[1], callback_data=user_list[1]),
    InlineKeyboardButton(user_list[2], callback_data=user_list[2]),
    InlineKeyboardButton(user_list[3], callback_data=user_list[3]),
  )
  return markup

def markup_inline_winkong():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton(user_list[0], callback_data=user_list[0]+"kong"),
    InlineKeyboardButton(user_list[1], callback_data=user_list[1]+"kong"),
    InlineKeyboardButton(user_list[2], callback_data=user_list[2]+"kong"),
    InlineKeyboardButton(user_list[3], callback_data=user_list[3]+"kong")
  )
  return markup

def markup_inline_winbite():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton(user_list[0], callback_data=user_list[0]+"bite"),
    InlineKeyboardButton(user_list[1], callback_data=user_list[1]+"bite"),
    InlineKeyboardButton(user_list[2], callback_data=user_list[2]+"bite"),
    InlineKeyboardButton(user_list[3], callback_data=user_list[3]+"bite")
  )
  return markup

def markup_inline_points():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton("1", callback_data="1_pt"),
    InlineKeyboardButton("2", callback_data="2_pt"),
    InlineKeyboardButton("3", callback_data="3_pt"),
    InlineKeyboardButton("4", callback_data="4_pt"),
    InlineKeyboardButton("5", callback_data="5_pt")
  )
  return markup

def markup_inline_shooter():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton(user_list[0], callback_data=user_list[0]+"_shoot"),
    InlineKeyboardButton(user_list[1], callback_data=user_list[1]+"_shoot"),
    InlineKeyboardButton(user_list[2], callback_data=user_list[2]+"_shoot"),
    InlineKeyboardButton(user_list[3], callback_data=user_list[3]+"_shoot"),
    InlineKeyboardButton("self-touch", callback_data="self_touch")
  )
  
  return markup

def markup_inline_kong():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton("明杠", callback_data="open_kong"),
    InlineKeyboardButton("暗杠", callback_data="hidden_kong")
  )
  return markup

def markup_inline_shootkong():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton(user_list[0], callback_data=user_list[0]+"shootkong"),
    InlineKeyboardButton(user_list[1], callback_data=user_list[1]+"shootkong"),
    InlineKeyboardButton(user_list[2], callback_data=user_list[2]+"shootkong"),
    InlineKeyboardButton(user_list[3], callback_data=user_list[3]+"shootkong"),
    InlineKeyboardButton("self-touch", callback_data="self_touchkong")
  )
  
  return markup

def markup_inline_bite():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
    InlineKeyboardButton("明咬", callback_data="open_bite"),
    InlineKeyboardButton("暗咬", callback_data="hidden_bite")
  )
  return markup

@bot.callback_query_handler(func=lambda message:True)
###########################################################################################
#markup_line()
def callback_query(call):
  global winner, points, kong
  if call.data == "win":
    bot.send_message(call.message.json['chat']['id'], "Winner?", reply_markup = markup_inline_win())

  elif call.data == "kong":
    bot.send_message(call.message.json['chat']['id'], "Winner?", reply_markup = markup_inline_winkong())

  elif call.data == "bite":
    bot.send_message(call.message.json['chat']['id'], "Winner?", reply_markup = markup_inline_winbite())


#########################################################################################
#markup_line_win()  
  elif call.data == user_list[0]:
    winner=user_list[0]
    bot.send_message(call.message.json['chat']['id'], "Points?", reply_markup = markup_inline_points())
    
  elif call.data == user_list[1]:
    winner=user_list[1]
    bot.send_message(call.message.json['chat']['id'], "Points?", reply_markup = markup_inline_points())

  elif call.data == user_list[2]:
    winner=user_list[2]
    bot.send_message(call.message.json['chat']['id'], "Points?", reply_markup = markup_inline_points())

  elif call.data == user_list[3]:
    winner=user_list[3]
    bot.send_message(call.message.json['chat']['id'], "Points?", reply_markup = markup_inline_points())

  elif call.data == "1_pt":
    points = 1
    bot.send_message(call.message.json['chat']['id'], "Shooter?", reply_markup = markup_inline_shooter())
    
  elif call.data == "2_pt":
    points = 2
    bot.send_message(call.message.json['chat']['id'], "Shooter?", reply_markup = markup_inline_shooter())

  elif call.data == "3_pt":
    points = 4
    bot.send_message(call.message.json['chat']['id'], "Shooter?", reply_markup = markup_inline_shooter())

  elif call.data == "4_pt":
    points = 8
    bot.send_message(call.message.json['chat']['id'], "Shooter?", reply_markup = markup_inline_shooter())

  elif call.data == "5_pt":
    points = 16
    bot.send_message(call.message.json['chat']['id'], "Shooter?", reply_markup = markup_inline_shooter())

  elif call.data == user_list[0]+"_shoot":
    loser = user_list[0]
    user[winner] += round(float(points*4*bet),2)
    user[loser] -= round(float(points*4*bet),2)
    display_score(call.message)

  elif call.data == user_list[1]+"_shoot":
    loser = user_list[1]
    user[winner] += round(float(points*4*bet),2)
    user[loser] -= round(float(points*4*bet),2)
    display_score(call.message)

  elif call.data == user_list[2]+"_shoot":
    loser = user_list[2]
    user[winner] += round(float(points*4*bet),2)
    user[loser] -= round(float(points*4*bet),2)
    display_score(call.message)

  elif call.data == user_list[3]+"_shoot":
    loser = user_list[3]
    user[winner] += round(float(points*4*bet),2)
    user[loser] -= round(float(points*4*bet),2)
    display_score(call.message)

  elif call.data == "self_touch":
    user[winner] += round(float(points*4*bet*1.5),2)

    for loser in user.keys():
      if loser != winner:
        user[loser] -= round(float(points*4*bet*0.5),2)
    display_score(call.message)

########################################################################################
#markup_inline_winkong()
  elif call.data == user_list[0]+"kong":
      winner=user_list[0]
      bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_kong())
      
  elif call.data == user_list[1]+"kong":
    winner=user_list[1]
    bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_kong())

  elif call.data == user_list[2]+"kong":
    winner=user_list[2]
    bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_kong())

  elif call.data == user_list[3]+"kong":
    winner=user_list[3]
    bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_kong())

  elif call.data == "open_kong":
    kong = "open"
    bot.send_message(call.message.json['chat']['id'], "Shooter?", reply_markup = markup_inline_shootkong())

  elif call.data == user_list[0]+"shootkong":
    loser = user_list[0]
    user[winner] += round(float(bet*3),2)
    user[loser] -= round(float(bet*3),2)
    display_score(call.message)

  elif call.data == user_list[1]+"shootkong":
    loser = user_list[1]
    user[winner] += round(float(3*bet),2)
    user[loser] -= round(float(3*bet),2)
    display_score(call.message)

  elif call.data == user_list[2]+"shootkong":
    loser = user_list[2]
    user[winner] += round(float(3*bet),2)
    user[loser] -= round(float(3*bet),2)
    display_score(call.message)

  elif call.data == user_list[3]+"shootkong":
    loser = user_list[3]
    user[winner] += round(float(3*bet),2)
    user[loser] -= round(float(3*bet),2)
    display_score(call.message)

  elif call.data == "self_touchkong":
    user[winner] += round(float(3*bet),2)

    for loser in user.keys():
      if loser != winner:
        user[loser] -= round(float(bet),2)
    display_score(call.message)
  
  
  elif call.data == "hidden_kong":
    user[winner] += round(float(6*bet),2)
    for loser in user.keys():
      if loser != winner:
        user[loser] -= round(float(2*bet),2)

    display_score(call.message)
##########################################################
#win bite
  elif call.data == user_list[0]+"bite":
      winner=user_list[0]
      bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_bite())
      
  elif call.data == user_list[1]+"bite":
    winner=user_list[1]
    bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_bite())

  elif call.data == user_list[2]+"bite":
    winner=user_list[2]
    bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_bite())

  elif call.data == user_list[3]+"bite":
    winner=user_list[3]
    bot.send_message(call.message.json['chat']['id'], "Which?", reply_markup = markup_inline_bite())

  elif call.data == "open_bite":
    user[winner] += round(float(3*bet),2)
    for loser in user.keys():
      if loser != winner:
        user[loser] -= round(float(bet),2)

    display_score(call.message)
  
  elif call.data == "hidden_bite":
    user[winner] += round(float(6*bet),2)
    for loser in user.keys():
      if loser != winner:
        user[loser] -= round(float(2*bet),2)
    
    display_score(call.message)
    


bot.polling()

"""
@bot.message_handler(commands=[''])
def (message):
  bot.send_message(message)
"""