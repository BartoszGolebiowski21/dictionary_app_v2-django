# dictionary_app_v2-django
Developed version of the dictionary_app. The current version has been created in Django.

Dictionary App
The Dictionary App is a web application built with the Django framework. It's a tool that allows users to store, browse, and test words in different languages along with their translations. Below, you'll find information about the setup, features, and how to use this application.

Requirements
Before you start using the application, make sure you have the following tools installed:

Python 3.11.4
Django 4.2.4
Other dependencies listed in the requirements.txt file

Installation
Clone the repository with the source code of the application:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd project_name
Install the required dependencies:

Copy code
pip install -r requirements.txt
Run database migrations:

Copy code
python manage.py migrate
Start the development server:

Copy code
python manage.py runserver
Open a web browser and go to http://localhost:8000/ to start using the application.

Using the App
The Dictionary App provides the following features:

Home Page: When you first access the application, you'll be redirected to the home page, where you can find general information about the app.

Dictionary Overview: Click on "Dictionary Overview" in the navigation menu to browse all the words available in the dictionary. You can also perform searches using the search field.

Add a Word: Use the "Add a Word" option in the navigation menu to add new words to the dictionary. You need to provide the word's translation in both English and Polish.

Word Details: Clicking on a specific word in the dictionary overview will take you to a page with detailed information about that word.

Edit a Word: You can edit a word by selecting the "Edit" option on the word's detail page.

Delete a Word: If you want to remove a word, you can do so from the word's detail page.

Test Your Words: By choosing "Test Your Words" in the navigation menu, you can test your knowledge. The app will randomly select a word, and you'll have to provide its translation. Your answer will be evaluated.

Authors
This application was created by [Your Name]. If you have questions or need assistance, please contact us at [Your Email Address].

License
This project is licensed under the [License Name]. For more information, see the LICENSE file.

Future Development
The Dictionary App is an ongoing project. We plan to add new features and improvements. If you have ideas for enhancing this application, we'd love to hear your suggestions.

Thank you for using the Dictionary App!
