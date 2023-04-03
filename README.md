# Blog

Blog is a web application created to practice working with Flask, database and Bootstrap.

To use application you need to download the content of repository and install libraries included in the requirements.txt file. Then run file blog.py, open the browser and go to http://localhost:5000 which is the main page of application.

The home page contains entries generated using Faker library. The functions of adding new posts, editing and deleting the existing one are restircted for logged in user. Once logged in, the user also gets access to the list of draft entries and possibility to publish them on a main page. All information is stored in database created using SQLAlchemy with a SQLite base.

The versions of used languages and libraries are contained in requirements.txt file.