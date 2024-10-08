city=["mumbai","hyderabad","Chennai","Pune","Ahmedabad","Bangalore","Delhi","Kolkata","Jaipur"]
print(city);
x=int(input("enter city no.(1-9) to remove to remove: "))
if x==1:
        city.remove("mumbai")
elif x==2:
          city.remove("hyderabad")
elif x==3:
          city.remove("Chennai")
elif x==4:
          city.remove("Pune")
elif x==5:
          city.remove("Ahmedabad")
elif x==6:
          city.remove("Bangalore")
elif x==7:
          city.remove("Delhi")
elif x==8:
          city.remove("Kolkata")
elif x==9:
          city.remove("Jaipur")
else:
    print("try again with a number from 1-9!")

print("after:     ");
print(city)