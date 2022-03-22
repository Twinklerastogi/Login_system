import hashlib
import get_data
import os    


def signup():
     email = input("Enter email address: ")
     pwd = input("Enter password: ")
     confirm_pwd = input("Confirm password: ")
     if confirm_pwd == pwd:
         encode_pwd = confirm_pwd.encode()
         hash1 = hashlib.md5(encode_pwd).hexdigest()
         with open("credentials.txt", "a") as f:
            f.write(email + "\n")
            f.write(hash1 + "\n")
         f.close()
         print("You have registered successfully!")
     else:
         print("Password is not same as above! \n")


def login():
     email = input("Enter email: ")
     pwd = input("Enter password: ")
     auth = pwd.encode()
     auth_hash = hashlib.md5(auth).hexdigest()
     with open("credentials.txt", "r") as f:
         stored_email, stored_pwd, *other = f.read().split("\n")
     f.close()
     
     if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         while 1:
             print("********** Welcome **********")
             print("1.Create User")
             print("2.Update User")
             print("3.Delete Users")
             print("4.Display All Users")
             print("5.Weather info")
             print("6.Go To Main Menu")
             try:
                 ch = int(input("Enter your choice: "))
             except:
                 print("Please enter valid input")
                 ch = 6
             if ch == 1:
                 signup()
             elif ch == 4:
                 file = fn = open('credentials.txt', 'r')
                 for index, line in enumerate(file.readlines()):
                     if (index%2==0):
                         print(line)
             elif ch == 3:
                 f = open('credentials.txt', 'r+')
                 f.truncate(0)
                 print("All users are deleted")
             elif ch == 5:
                 weather_info()
             elif ch == 6:
                 break
     else:
         print("Login failed! Please enter correct email or password\n")


def weather_info():
    data = get_data.api_data()
    # print(data)
    if data["cod"] != "404":
         result = data["main"]
         avg_temperature = (result["temp_min"] + result["temp_max"]) / 2
         current_pressure = result["pressure"]
         current_humidity = result["humidity"]
         wind_details = data["wind"]
         wind_speed =  wind_details["speed"]
         wind_degree = wind_details["deg"]
         print("****** Weather *******")
         print("Humidity = " +
                    str(current_humidity) + " %" +
            "\nAtmospheric pressure = " +
                    str(current_pressure) + " hPa" +
            "\nAverage Temperature = " +
                    str(avg_temperature) + " kelvin" +
            "\nWind Speed = " +
                    str(wind_speed) + " m/s" + 
            "\nWind Degree = " +
                    str(wind_degree))
    else:
        print(" City Not Found ")
    

   
while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    try:
        ch = int(input("Enter your choice: "))
    except:
        print("Please Enter Valid Input")
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
