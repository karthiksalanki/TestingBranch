# Stazi Technologies Private Limited

REQUIREMENTS:
<br/>
<ul>
  <li>Python 3</li>
  <li>MySQL</li>
  <li>Django (install by PIP 'pip install django' and install 'pip install djangorestframework')</li>
  <li>MySQL db (install by PIP 'pip install mysqlclient' and create database name'auctionapp' or configure the database)</li>
  </ul>
  <br/>
  Steps to run application:
<ul>
<li>first, run the commands 'python manage.py makemigrations' and 'python manage.py migrate' to create the tables</li>
 <li> Create admin by using 'python manage.py createsuperuser' and to run the server 'python manage.py runserver'</li>
<li>Login by admin to create the auctions and to see the bids(login at 'http://127.0.0.1:8000/admin/')</li>
<li>To check whether the auction is closed or not we need to hit this 'http://127.0.0.1:8000/auctions/complete/' end point</li>
</ul>