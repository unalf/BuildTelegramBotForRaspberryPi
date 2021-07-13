# encoding:utf-8

# Import Libraries
import time
import threading
import telebot
import gpiozero

# Initial Conditions
ALARM_SET = 0                             #When device starts, default is no alarm set.
USER_NAME = 'YOUR_TELEGRAM_USER_NAME'     #Enter your telegram username.

# Set Raspberry Pi GPIO
pir1 = gpiozero.DigitalInputDevice(17)    #GPIO17, PASSIVE INFRARED SENSOR 1
pir2 = gpiozero.DigitalInputDevice(25)    #GPIO25, PASSIVE INFRARED SENSOR 2
alarm = gpiozero.DigitalOutputDevice(24)  #GPIO24, ALARM WARNING SIREN
cpu = gpiozero.CPUTemperature()           #RASPBERRY CPU TEMPERATURE

# Initial Conditions
alarm.off()                               #When device starts, turn off alarm.

# Telebot API Configuration
chat_id = "TELEGRAM_CHAT_ID_THAT_YOU_OBTAINED"             #Enter telegram chat id (that your bot joined). Like -0000000000000
bot_status_flag = 0
while bot_status_flag==0:
    try:
        bot = telebot.TeleBot("TOKEN_KEY_THAT_YOU_OBTAINED") #Enter token you obtained from Telegram BotFather.
        bot.send_message(chat_id,'DEVICE IS RESTARTED. ALL ALARM ORDERS ARE RESET.')
        bot_status_flag = 1
    except:
        time.sleep(5)
        print("Error at Telebot API Configuration")

# Listen PIR and Activate Alarm Every Seconds
def listen_PIR():
  while True:
      try:
          if (pir1.value==1) & (pir2.value == 1):
            MOTION_DETECTED = 1 #BOTH PIR1 & PIR2 DETECTED
            MOTION_STRING = 'MOTION_DETECTED: PIR1 and PIR2.'
          elif (pir1.value==1) & (pir2.value == 0):
            MOTION_DETECTED = 2 #ONLY PIR1 DETECTED
            MOTION_STRING = 'MOTION_DETECTED: PIR1.'
          elif (pir1.value==0) & (pir2.value == 1):
            MOTION_DETECTED = 3 #ONLY PIR2 DETECTED
            MOTION_STRING = 'MOTION_DETECTED: PIR2.'
          elif (pir1.value==0) & (pir2.value == 0):
            MOTION_DETECTED = 0 #NO MOTION
            MOTION_STRING = 'NO MOTION'

          if (ALARM_SET==1) & (MOTION_DETECTED>0) & (alarm.value ==0):
            alarm.on() #START SIREN AT LEAST FOR 15 SECONDS EVEN PIR SIGNAL DISAPPEARS
            bot.send_message(chat_id, 'SIREN IS ACTIVE. MOTION DETECTED! '+ MOTION_STRING)
            time.sleep(15)

          if (MOTION_DETECTED==0) & (alarm.value == 1):
            alarm.off() #STOP ALARM ORDER
            bot.send_message(chat_id, 'SIREN IS STOPPED! '+ MOTION_STRING)

          if (ALARM_SET==0) & (alarm.value ==1):
            alarm.off() #STOP SIREN ORDER
            bot.send_message(chat_id, 'SIREN IS STOPPED BY YOUR ORDER! '+ MOTION_STRING)
      except:
        print("Error at Listen PIR Function.")
      time.sleep(1)

# Telegram Polling
def telegram_polling():
    while True:
        try:
            bot.polling(none_stop=True, interval=2) #Polling every 2 seconds.
        except:
            time.sleep(5)
            print("Error at Telegram Polling Function.")

# Telegram Check Orders
@bot.message_handler()
def check_orders(message):
  global ALARM_SET
  try:
      if (message.from_user.username == USER_NAME) & (message.text == 'homestatus'):
         bot.send_message(chat_id, 'STATUS: '+ str(siren.value) + '. PIR1: ' + str(pir1.value) + '. PIR2: ' + str(pir2.value))
      elif (message.from_user.username == USER_NAME) & (message.text == 'on'):
        ALARM_SET = 1 #START ALARM
        bot.send_message(chat_id,'ALARM IS ACTIVATED.')
      elif (message.from_user.username == USER_NAME) & (message.text == 'off'):
        ALARM_SET = 0 #STOP ALARM
        bot.send_message(chat_id,'ALARM IS DEACTIVATED BY YOUR ORDER.')
      elif (message.from_user.username == USER_NAME) & (message.text == 'cputemp'):
        bot.reply_to(message, 'PI CPU TEMPERATURE: ' + str(cpu.temperature))
      elif (message.from_user.username == USER_NAME):
        bot.reply_to(message, 'TYPE ERROR. PLEASE USE: homestatus, on, off, cputemp.')    
  except:
    print("Error at Telegram Check Orders Function.")

#Start Threading
thread1 = threading.Thread(target=listen_PIR)
thread2 = threading.Thread(target=telegram_polling)
thread1.start()
thread2.start()
