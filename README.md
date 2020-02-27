# KL ExchangeRates
A bot to send USD to MYR Exchange rates in Kuala Lumpur, Malaysia to a telegram chat

## Getting Started

The following will help setup the bot that can run every hour and send the exchange rates to your telegram chat.

### Prerequisites
```
pip install -r requirements.txt
```

### Installing

In order to run the bot you need a Telegram app. You can create one from my.telegram.org 

Once you have an app, create the env.py file using the env.py.example in the repo

```
cp env.py.example env.py && nano env.py
```

Fill in your App details and the Chat ID or the Username of the chat to use.

One done, you can run the bot using the following commands. 

Start a screen session

```
screen -S klbot
```
Run the bot
```
python bot.py
```
Press `Ctrl+a d` to detach from the screen session


## Authors

* **Mohamed Aruham** - [PhoneixAtom](https://github.com/PhoenixAtom)

## Acknowledgments

* Ashraq for the suggestion
* klmoneychanger for the rates
