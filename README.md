
# Wifi Pineapple Wardriving 📡🍍

A Tool for wardriving with the Wifi Pineapple using iOS or Android, Data is exported to kml format so it can be loaded to google maps and such.

## Why?

Ever wanted to go wardriving with the WiFi pineapple but you didn't want to buy a gps receiver? or you have iOS? why not use your phone's gps receiver?

## Demo

Insert gif or link to demo


## FAQ

#### How do I use it?

there are 2 files that you need to run **on the wifi pineapple**.

wardrive.py which is responsible for authentication and scanning. \
webserver.py  which is responsible for the web server that you connect to from your phone so wardrive.py can know your current location.

once your mobile device is connected to the WiFi pineapple's managment AP you navigate to https://pineappleIP:8000/ from your phone and allow location tracking.

#### How do I stop it?

You can just stop the files with ctrl+c, the pineapple scan will be stopped automatically and the wardriving data will be saved to wardriveData.kml

#### Do I need internet connection for it?

once you install the program on the Wifi Pineapple you don't need internet connection, you just need your phone to connect to the web server.

#### What happens if the Wifi Pineapple disconnectes?

Every time there is new Data the program saves it, so if the pineapple disconnects mid scan you won't lose any unsaved data.

#### What Data does the program collect?

The program collect the following data all from the Wifi Pineapple api.

 - ssid
 - bssid
 - Operated Channel
 - Signal Strength
 - isHidden
 - isWPS
## Installation

Installation is done in the Wifi Pineapple

```bash
  git clone https://github.com/ozzzozo/wardriving.git
  cd wardriving
  pip install -r requirements.txt
```
    
## Usage

```bash
python3 webserver.py
python3 wardrive.py -u pineappleUser -P pineapplePassword
```

you can also run `python3 wardrive.py -h` for more details and options.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Note

This program was tested on the Wifi Pineapple MK7 with Firmware v1.1.1
