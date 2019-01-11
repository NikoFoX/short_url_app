Django Test Application.

Given the URL the form should check DB for existing entry of that URL.
If URL not found in DB, app should add new entry.

Submitters are fetched randomly from database by custom manage.py command and randomly bound to new entry.


Use:

0) Fill User DB table with X users by executing ./manage.py create_fake_users X
It fetches data from randomuser.me and insert into DB User table.
Without any user added, the app will give error.

1) Run app and enter localhost/ to see the app.

2*) Add new website to DB
Insert URL into input and choose how many characters should be generated.

3) At /XXXX/submitted you will see XXXX - the generated short URL which you can use.

The short link example: localhost/3GHH.

*Entering the same URL gets you to the page with already generated short URL.

To check where does the short URL directs to, before actually directing to the original URL, prepend the URL with "!" sign, for example localhost/!3GHH.
