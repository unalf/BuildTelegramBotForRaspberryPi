# Telegram Bot for Raspberry Pi
With Telegram (pyTelegramBotAPI) control your Raspberry Pi for smart home projects. You can send and receive information to/from Raspberry Pi, activate/deactivate GPIO's on the card. Telegram is a very efficient way to conduct a two way communication. 

In this example a home alarm control is conducted with Raspberry Pi with following hardware:
  1. Raspberry Pi
  2. 2 x Passive Infrared Sensor
  3. Alarm Siren
  4. Power Supplies, Cables, Relay with Control Card, etc...

To control Raspberry Pi GPIO, gpiozero library is used. For further info on library, visit:
[https://gpiozero.readthedocs.io/en/stable/]

For passive infrared sensor (pir1) GPIO17 and for passive infrared sensor (pir2) GPIO25 is used as digital input device.

```python
pir1 = gpiozero.DigitalInputDevice(17)    #GPIO17, PASSIVE INFRARED SENSOR 1
pir2 = gpiozero.DigitalInputDevice(25)    #GPIO25, PASSIVE INFRARED SENSOR 2
```

For activating/deactivating alarm siren, GPIO24 is used  as digital output device.

```python
alarm = gpiozero.DigitalOutputDevice(24)  #GPIO24, ALARM WARNING SIREN
```

To track Raspberry Pi's CPU temperature cpu object is used. Useful to observe card temperature at hot weather conditions.

```python
cpu = gpiozero.CPUTemperature()           #RASPBERRY CPU TEMPERATURE
```

Before starting, you should create a Telegram Bot using BotFather. The steps are:

1. Find @BotFather at Telegram.
2. Type /start
3. Type /newbot
4. Enter your bot name.
5. Save your token to access API.

You will send orders to telegram bot and bot will reply to a chat group. This will allow multiple users to track alarm status of the home. I advice you to create a private Telegram group and join bot to the group that you've created. Once you create group, save your group chat id. To get group chat id, you can use: [https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id]

Enter your Telegram username below, this step will allow script to take orders only from you.

```python
USER_NAME = 'YOUR_TELEGRAM_USER_NAME'     #Enter your telegram username.
```
OK. Now the bot is ready, chat group is ready, hardware is OK. Let's start communicating!

Here are the orders:

1. **homestatus**: bot sends current status of pir sensors and alarm siren.
2. **on**: activates alarm.
3. **off**: deactivates alarm.
4. **cputemp**: bot sends current CPU temperature of the Raspberry.

For Telegram polling function and listening alarm, threading is used, for further information on threading visit https://docs.python.org/3/library/threading.html.

You need 4 Python libraries for this project:
1. time       [https://docs.python.org/3/library/time.html?highlight=time#module-time]
2. threading  [https://docs.python.org/3/library/threading.html]
3. telebot    [https://github.com/eternnoir/pyTelegramBotAPI]
4. gpiozero   [https://gpiozero.readthedocs.io/en/stable/]

That's all. Now you can activate/deactivate alarm, track status and get message when motion is detected with Raspberry Pi and Telegram.
