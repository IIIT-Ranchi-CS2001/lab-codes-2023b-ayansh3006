Name = str(input("Enter Name : "))
Roll = int(input("Enter Roll no. : "))
Marks = float(input("Enter Marks :"))

print(Name)
print(Roll)
print(Marks)
 
if(Marks >= 90):
    print("Grade point : 10" )
    print("Remark : Outstanding")

elif( 90> Marks >=80):
    print("Grade point : 9" )
    print("Remark : Very Good")

elif( 80 > Marks >= 70):
    print("Grade point : 8" )
    print("Remark : Good")

elif( 70> Marks >=60):
    print("Grade point : 7" )
    print("Remark : Average")

elif(60 > Marks >= 50):
    print("Grade point : 6" )
    print("Remark : Pass")

elif( Marks < 50):
    print("Grade point : 0" )
    print("Remark : Fail")