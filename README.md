# MailManagerBot

*This Telegram bot can create new mail accounts if running on a vserver like Uberspace.*

## Setup (Linux)
1. Clone this repository  
`git clone https://github.com/Andre0512/MailManagerBot && cd MailManagerBot`
2. Create virtual environment (optional)  
`python3 -m venv venv && source veve/bin/activate`
3. Install requirements  
`pip install -r requirements.txt`
4. Set custom configs in `config.py`  
`cp config.py.default config.py && vim config.py`
5. Run bot
`./MailManagerBot.py &`  

## License
This project is under MIT license. Have fun :)
