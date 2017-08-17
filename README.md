```

                        _______   _   ________  _                                  
                        |_   __ \ (_) |_   __  |(_)                                 
                          | |__) |__    | |_ \_|__   _ .--.   .--./) .---.  _ .--.  
                          |  ___/[  |   |  _|  [  | [ `.-. | / /'`\;/ /__\[ `/'`\] 
                         _| |_    | |  _| |_    | |  | | | | \ \._//| \__., | |     
                        |_____|  [___]|_____|  [___][___||__].',__`  '.__.'[___]    
                                                            ( ( __))    

                         [---]   Just for fun and security @octosec    [---]
                         [---]   W:besimaltinok.com | T:altnokbesim    [---]
                         [---]                G:besimaltnok            [---]
                         ---------------------------------------------------

```

### About Project

The purpose of this project is to determine whether the network we are connected for is opened by Wifi- Pineapple. In addition, we analyze wireless networks you have previously connected and give you a security score.

### Features

* Is this network opened by pineapple?
* Have we been connected to insecure networks before?
* Logging  (
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `HTTP Port Screenshot`
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `Wireless Security Score`)

### Used Techinuques

**WiFi-Pineapple Network Detection Techniques**

```
A Chinese proverb says:
"If attackers are accessing systems using default settings, 
we too can catch them with the default settings in their software and hardware."
```

* Manufacturer's MAC address information
* Default HTTP Port (1471)
* Default hostname information for wifi-pineapple

**Previous networks**

* Analyzes the wireless networks you have previously connected

### Usage

#### Requirements

* **Modules:** scapy, time, termcolor, sys
* **OS:** Kali, Ubuntu

Download pisavar:

`git clone https://github.com/besimaltnok/PiFinger.git`

Install Python librarie(s):

`pip install termcolor`

It's done!

Run the program with following command: 

Run:

```python
cd PiFinger
python pifinger.py
```

### Screenshots
<p align="center">
<img src="images/interface.png" width="45%"></img>
<img src="images/log.png" width="45%"></img>
</p>
---------------------------------------------------------------------------
<p align="center">
<img src="images/pifinger.png" width="45%"></img>
<img src="images/notpi.png" width="45%"></img>
</p>

### Demo Video

- Video

### Authors
This project is coded by Besim ALTINOK
