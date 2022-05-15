import subprocess
if __name__ == '__main__':
    subprocess.run('pip install django'.split())
    subprocess.run('python inventory_web_app/manage.py runserver 0.0.0.0:8000'.split())
