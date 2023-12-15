# Flask App Setup

This guide outlines the steps to set up a Flask web application on a Ubuntu server using Apache as the web server and mod_wsgi as the interface between Apache and Flask. The example assumes that you have a Flask application located in `/var/www/Youtube_Summary_Generator` and a domain named `flaskapp.example.com`.

## Prerequisites

Before starting the setup process, ensure that your system is up-to-date and has the necessary packages installed:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3 python3-pip python3-venv
sudo apt-get install apache2 libapache2-mod-wsgi-py3
```

## Setting Up Flask App

1. Create the Flask app directory:

```bash
cd /var/www/
git clone https://github.com/mrashutoshnigam/Youtube_Summary_Generator.git
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required Python packages:

```bash
cat requirements.txt | xargs -n 1 pip install
```

4. Set the Flask app environment variable:

```bash
export FLASK_APP=app.py
```

## Configure mod_wsgi

1. Create a mod_wsgi script file:

```bash
nano /var/www/Youtube_Summary_Generator/flaskapp.wsgi
```

Add the following content to the file:

```python
import sys
import logging

sys.path.insert(0, '/var/www/Youtube_Summary_Generator')
sys.path.insert(0, '/var/www/Youtube_Summary_Generator/venv/lib/python3.10/site-packages/')

# Set up logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# Import and run the Flask app
from app import app as application
```

Save and exit the editor.

## Configure Apache

1. Create an Apache virtual host configuration file:

```bash
sudo nano /etc/apache2/sites-available/flaskapp.example.com.conf
```

Add the following content to the file:

```apache
<VirtualHost *:443>
    ServerName flaskapp.example.com
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/Youtube_Summary_Generator

    WSGIDaemonProcess flaskapp threads=5
    WSGIScriptAlias / /var/www/Youtube_Summary_Generator/flaskapp.wsgi
    WSGIApplicationGroup %{GLOBAL}
    
    <Directory flaskapp>
        WSGIProcessGroup flaskapp
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/flaskapp-error.log
    CustomLog ${APACHE_LOG_DIR}/flaskapp-access.log combined
</VirtualHost>
```

Save and exit the editor.

2. Enable the virtual host:

```bash
sudo a2ensite flaskapp.example.com
```

3. Restart Apache to apply the changes:

```bash
sudo service apache2 restart
```

Your Flask app should now be accessible at `https://flaskapp.example.com`. Ensure that your domain is properly configured to point to the server's IP address.