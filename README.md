# DEATHS_IN_YEAR
This python script is designed to send messages to mail via smtp protocol. <p>
Script reports new deaths based on Wikipedia article [Deaths_in_2023](https://en.wikipedia.org/wiki/Deaths_in_2023)
#### Git

Clone the repository
```
git clone https://github.com/Alexander671/Deaths-in-Year/
```

Navigate into the `Deaths-in-Year` directory
```
cd Deaths-in-Year
```

#### .env file

For correct work you need to create .env file in `~/PROJECT_DIR/Deaths-in-Year/.env` or rename `.env copy` to `.env` file
with the following content:

```
nano .env 
```

```
SENDER_EMAIL="{your_email}"
RECEIVER_EMAIL="{reciever_email}"
SMTP_PASSWORD="{your_password_smtp}"
SMTP_PORT=465
SMTP_USERNAME="Deaths_in_2023"
SMTP_SERVER="smtp.yandex.com.tr"
# if this is the first run, is it necessary to receive all previous messages
SEND_OLD_UPDATES=False
LOGFILE="output.log"
```

#### Dependencies

Install, using `pip` (beeter use with virtual environments: example `venv`):

```
pip install -r requirements.txt
```


#### Usage
enter the following command
```
cd src/
python3 main.py
```
after that the script will be detached and will run in an infinite loop <p>
enter the following command if you want to see how the program is running
```
ps axuw | grep main.py
```

and following to kill the process
```
kill {pid}
```

#### Essay
[Death - Google Docs](https://docs.google.com/document/d/1c2kwByoR2hJ1fbw9SPGEYEIcI7yQkQSdJGtWQgezokw/edit)
