# api
Clone api repo to your system

```bash
https://github.com/SanVik132/api.git
```

## Installation

Create a virtual environment to run the project:

```bash
python3 -m venv venv
```


activate the virtual environment:

```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Running Project

Change your directory to project directory and run the following command:

```python
python manage.py runserver
```

## Usage
Please navigate to urls.py for all links.


## api urls



#a user will be created with all permissions,can manage everything
Url : http://127.0.0.1:8000/
Request:Post
Data:
{
    "mobile":"1234567890",
    "email":"vikramjeetlg@gmail.com",
    "first_name":"Vikramjeet",
    "password":"demo123@"
}

Url : http://127.0.0.1:8000/accounts/register/confirm/
Request:Post
Data:
{
    "mobile":"1234567890",
    "otp":"123456" #by default otp for testing is 123456
   
}


#forgot password view

url :http://127.0.0.1:8000/forgotpassword/    
Request:post
data:
{
    "mobile":"8901388132"
}

url :http://127.0.0.1:8000/forgotpassword/confirm/
Request:post
Data:
{
    "mobile":"8901388132",
    "otp":"123456"
}

url :http://127.0.0.1:8000/newpassword/
Request:post
Data:
{
     "password":"Demo123@@"
}

+JWT for authentication


url http://127.0.0.1:8000/student/
Request:GET



url http://127.0.0.1:8000/student/
Request :Post
data
{
    "admission_number":"123456567",
    "firstname":"Vikram",
    "lastname":"Jeet",
    "gender":"male",
    "blood_group":"B+",
    "date_of_birth":"1998-01-18",
    "address":"demo",
    "parent_mobile_number":"8572881328"

}

url http://127.0.0.1:8000/student/<int:id>/
request :GET
Will return single user with id

url http://127.0.0.1:8000/student/<int:id>/
request Delete
will delete user 

url http://127.0.0.1:8000/student/<int:id>/
Request PUT
data

url http://127.0.0.1:8000/teacher/
Request Post

Data
{
    "firstname":"Vikramjeet",
    "lastname":"Jeet",
    "address":"demo",
    "mobile_number":"8572881328"

}

## for details of student(self):
url http://127.0.0.1:8000/stdent-self/
method = GET