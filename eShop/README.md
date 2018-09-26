### share_project: Eshop project
Made by Trinh, Thu, Hung, Huy and Luc

###### Make new branch
git branch dev-huutrinh

###### Switch to new branch
git checkout dev-huutrinh

###### Confirm the current branch
git branch

###### Push source code to branch
git push origin dev-huutrinh

###### Show all list branchs
git branch -a   

###### Add remote git
git remote add origin git@github.com:2t2hl/share_project.git

###### Install library:
sh install.sh

###### How to run:
./manage.py makemigrations
./manage.py migrate
./manage.py runserver

###### TODO
* add tax rate
* stripe integrations
* show name country shipping


###### From here is optional:
###### Add shipping country
pip install pycountry
./manage.py oscar_populate_countries

###### Test visa
http://www.getcreditcardnumbers.com

###### Install stripe
pip install stripe

###### Reference URL
http://akiyoko.hatenablog.jp/entry/2016/05/31/014711
https://qiita.com/ytyng/items/a4ae77df8bc4c5506d19

###### Fake address
https://www.fakeaddressgenerator.com/World/us_address_generator

###### Show all tables in database
qlite3 db.sqlite3
.tables

