# api


#a user will be created with all permissions,can manage everything
Url : http://127.0.0.1:8000/accounts/register/
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

