# telegram-autotrader
Automatically trade signals from Telegram in Metatrader

# Installation

`PARENT_DIR` is a directory that is the parent of both the dependent repository
and this repo.

## Clone the dependent repository

    shell> cd $PARENT_DIR
    shell> git clone https://github.com/darwinex/dwx-zeromq-connector

### Follow the instructions in that README.md to get it setup
you need to do some unzipping and copying.

## Clone this repository
    shell> cd $PARENT_DIR
    shell> git clone https://github.com/metaperl/telegram-autotrader

## Install Python dependencies.
    shell> cd telegram-autotrader
    shell> pip install -r requirements.txt

## At this point you have two directories
Both below `PARENT_DIR` and sibling to each other.

### Configure Python's module import

Extend `PYTHONPATH`. On windows, I needed to add the following 2 paths:

    C:\cygwin64\home\terre\prg\telegram-autotrader\src;C:\cygwin64\home\terre\prg\dwx-zeromq-connector\v2.0.1\python\api

## Make sure that you can issue signals from Python to MT4

    shell> cd telegram-autotrader/src
    shell> python simple.py

## Now run the telegram_to_mt4.py

    shell> python telegram_to_mt4.py

# May the profits be with you!
