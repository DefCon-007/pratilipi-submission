# PratilipiPVR

A django application for the task of Pratlipi full stack postion. Website live at http://pratilipipvr.defcon007.com/

## Installation

Clone the repository locally. 
```bash
git clone https://github.com/DefCon-007/pratilipi-submission

```

Now create a virtual environment for the project 
```bash
pip3 install virtualenv
virtualenv -p python3 ./venvpvr
```

Activate the virtual environment
```bash 
source venvpvr/bin/activate
```


Install the required modules 
```bash
cd pratilipi-submission
pip install -r requirements.txt
```

Now make a local copy of the `config-template.ini` and complete the fields accordingly. (Postgresql database is recommended)
```bash
cp ./config-templat.ini ./config.ini
vim config.ini
```

Collect static django assets
```bash
python manage.py collectstatic
```

Run migrations
```bash
python manage.py migrate
```

Now everything is setup run `python manage.py runserver` to run the local development server.
