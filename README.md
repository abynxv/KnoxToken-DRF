# KnoxToken-DRF
This project demonstrates a basic implementation of Knox Token authentication using Django. It includes endpoints for user register, profile, login, logout and logoutall functionality. 
The Knox Token Authentication System is a secure authentication mechanism built using Django and the Django REST Framework. 
It provides token-based authentication for users accessing the application's endpoints, ensuring secure communication between clients and the server.

Setup Instructions

  ->Clone the Project-Create a directory, open a terminal in the directory path, and clone the  project:

      git clone https://github.com/abynxv/KnoxToken-DRF.git
      
  ->Install Virtual Environment
  
      pip install virtualenv
      
  ->Create a virtual environment within the directory:

      python -m venv venv_name  # On Windows
      python3 -m venv venv_name  # On macOS/Linux

  ->Activate Virtual Environment

      venv_name\Scripts\activate       # On Windows
      source venv_name/bin/activate    # On macOS/Linux

  ->Install Requirements

      pip install django djangorestframework django-rest-knox

  ->Open the project in VS Code:

      code .

  ->Open a terminal in VS Code, navigate to the project directory, and run the server:
  
      cd myproject
      python manage.py runserver
      
API Endpoints

1.Register

    Endpoint  : api/register/
    Method    : POST     - Register User
    Data      : JSON     - {"name": "string" , "password": "password"}
    
2.Login

    Endpoint  : api/login/
    Method    : POST     - User Login
    Data      : JSON     - {"name": "string", "password": "password"}
    
3.Profile

    Endpoint  : api/profile/
    Method    : POST     - Refresh Token
    Headers   - Key   :  Authorization
                Value :  Token "Your Access Token"
    
4.Logout(Current Session)

    Endpoint  : api/logout/
    Headers   - Key   :  Authorization
                Value :  Token "Your Access Token"

5.LogoutAll(Entire Session)

    Endpoint  : api/logoutall/
    Headers   - Key   :  Authorization
                Value :  Token "Your Access Token"
