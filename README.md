# TelegramBotForRaspberryPi
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

To track Raspberry Pi's CPU temperature cpu object is used.

```python
cpu = gpiozero.CPUTemperature()           #RASPBERRY CPU TEMPERATURE
```

Before starting, you should create a Telegram Bot using BotFather. The steps are:

1. Find @BotFather at Telegram.
2. Type /start
3. Type /newbot
4. Enter your bot name.
5. Save your token to access API.
