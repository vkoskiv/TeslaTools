
## TeslaTools - Simple tools for probing the Tesla Motors API.

## Requirements:

- Python3
- requests (pip3 install requests)

## Usage:

`./getToken.py <Your Tesla account email> <Your Tesla account password>`

This script will request a new token you can use for subsequent requests.  It will also store it in token.txt along with other useful info
If you've already acquired a token, it will just be retrieved from your `token.txt` file.

`./decoder.py <Your authentication token (acquire with getToken.py)>`

This script will retrieve a list of your vehicles and decode the feature codes to a readable format.

Example output for a 2017 Model S 75D:

~~~
MyModelS (XXXXXXXXXXXXXXXXX):
    ADPX2 = Type 2 Public Charging Connector
    ADX4  = Type 2 Public Charging Connector
    ADX6  = Type 2 Public Charging Connector
    ADX7  = Type 2 Public Charging Connector
    ADX8  = Blue IEC309 (1 phase, 230V 32A)
    AF00  = No HEPA Filter
    APF0  = Autopilot Firmware 2.0 Base
    APH3  = Autopilot 2.5 Hardware
    APPA  = Autopilot 1.0 Hardware
    AU00  = No Audio Package
    BCMB  = Black Brake Calipers
    BP00  = No Ludicrous
    BR00  = No Battery Firmware Limit
    BS00  = General Production Flag
    BTX5  = 75 kWh
    CDM0  = No CHAdeMO Charging Adaptor
    CF00  = No CHAdeMO Charging Adaptor
    CH04  = 72 Amp Charger (Model S/X)
    CW00  = No Cold Weather Package
    DCF0  = Autopilot Convenience Features (DCF0)
    DRLH  = Left Hand Drive
    DSH5  = PUR Dash Pad
    DU00  = Drive Unit - IR
    DV4W  = All-Wheel Drive
    FG02  = Exterior Lighting Package
    FMP6  = ?
    FR04  = ?
    HP00  = No HPWC Ordered
    IDBA  = Dark Ash Wood Decor
    INBTB = Multi-Pattern Black
    IX00  = No Extended Nappa Leather Trim
    LLP2  = ?
    LP01  = Premium Interior Lighting
    MDLS  = Model S
    ME02  = Memory Seats
    MI01  = 2016 Production Refresh
    PF00  = No Performance Legacy Package
    PI00  = No Premium Interior
    PK00  = LEGACY No Parking Sensors
    PPSB  = Deep Blue Metallic
    PS01  = Parcel Shelf
    PSPX4 = Parcel Shelf
    PX00  = No Performance Plus Package
    QTTB  = Multi-Pattern Black Seats
    REEU  = Region: Europe
    RFFG  = Glass Roof
    S31B  = ?
    SC05  = Free Supercharging
    SP01  = Free Supercharging
    SR07  = Standard 2nd row
    ST01  = Non-heated Leather Steering Wheel
    SU01  = Smart Air Suspension
    TM00  = General Production Trim
    TR00  = No Third Row Seat
    UTPB  = Dark Headliner
    WTAS  = 19" Silver Slipstream Wheels
    WTW2  = 19" Silver Slipstream Wheels
    WXW1  = 19" Silver Slipstream Wheels
    WXW3  = 19" Silver Slipstream Wheels
    X001  = Override: Power Liftgate
    X003  = Maps & Navigation
    X007  = Daytime running lights
    X011  = Override: Homelink
    X014  = Override: No Satellite Radio
    X021  = No Spoiler
    X025  = No Performance Package
    X027  = Lighted Door Handles
    X028  = Battery Badge
    X031  = Keyless Entry
    X037  = Powerfolding Mirrors
    X039  = DAB Radio
    X043  = No Phone Dock Kit
    YFCC  = ?
    COFI  = ?
~~~

## Security:

You should audit these scripts before providing your Tesla credentials.

## TODO:

- `getToken.py` should refresh the token if it's outdated automatically.
- New tools should be added.


