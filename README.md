# Dictionary App

The Dictionary App is a web application built with the Django framework. It's a tool that allows users to store, browse, and test words in different languages along with their translations. Below, you'll find information about the setup, features, and how to use this application.

## Requirements

Before you start using the application, make sure you have the following tools installed:

- Python 3.11.4
- Django 4.2.4
- Other dependencies listed in the `requirements.txt` file

## Installation

1. Clone the repository containing the source code for the application:

git clone https://github.com/BartoszGolebiowski21/dictionary_app_v2-django.git

2. Navigate to the project directory:

cd dict_project

3. Install the required dependencies:

pip install -r requirements.txt

4. Apply database migrations:

py manage.py makemigrations
py manage.py migrate

5. Start the development server:

python manage.py runserver

6. Open a web browser and access `http://localhost:8000/` to begin using the application.

## Using the App

The Dictionary App offers the following functionalities:

- **Home Page**: When you first access the application, you'll be redirected to the home page, where you can find general information about the app.

- **Show the entire dictionary**:  Click on "Show the entire dictionary" in the navigation menu to browse all the words available in the dictionary. You can also perform searches using the search field.

- **Add a new word**: Use the "Add a new word" option in the navigation menu to add new words to the dictionary. You need to provide the word's translation in both English and Polish.

- **Word details**: Clicking on a specific word in the dictionary overview will take you to a page with detailed information about that word.

- **Edit the word**: You can edit a word by selecting the "Edit" option on the word's detail page.

- **Delete the word**: If you want to remove a word, you can do so from the word's detail page.

- **Test mode**: By choosing "Test mode" in the navigation menu, you can test your knowledge. The app will randomly select a word, and you'll have to provide its translation. Your answer will be evaluated.

## Authors

This application was developed by Bartosz Gołębiowski.

## Future Development

The Dictionary App is an ongoing project. We plan to add new features and improvements. If you have ideas for enhancing this application, we'd love to hear your suggestions.

Thank you for choosing the Dictionary App!

