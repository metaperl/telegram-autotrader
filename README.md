# telegram-autotrader
Automatically trade signals from Telegram in Metatrader 4

# Installation

`PARENT_DIR` is a directory that is the parent of both the dependent repository
and this repo.

## Clone the dependent repository
    
    shell> cd $PARENT_DIR
    shell> git clone https://github.com/darwinex/dwx-zeromq-connector

### Follow the instructions in the README.md to get it setup
you need to do some unzipping and copying
    
## Clone this repository
    shell> cd $PARENT_DIR
    shell> git clone https://github.com/metaperl/telegram-autotrader
    
## Install Python dependencies.
    shell> cd telegram-autotrader
    shell> pip install -r requirements.txt

## Set the absolute path to dwx-zeromq-connector 
Edit 

## At this point you have two directories
Both below `PARENT_DIR` and sibling to each other.

## Make sure that you can issue signals from Python to MT4



    shell> cd telegram-autotrader/src
    shell> python simple.py


