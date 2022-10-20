from mini import DBhelper
def main():
    db=DBhelper()
    while True:
        print()
        print("Press 1 to insert new student")
        print("Press 2 to display all student")
        print("Press 3 to delete student")
        print("Press 4 to update student")
        print("Press 5 to exit program")
        print()
        try:
            choice=int(input())
            if (choice==1):
                s_id=int(input("Enter student id: "))
                studentName=input("Enter student name: ")
                phone=input("Enter phone number: ")
                db.insert_stu(s_id,studentName,phone)
            elif(choice==2):
                db.fetch_all()
            elif(choice==3):
                s_id=int(input("Enter student id to which you want to delete"))
                db.delete_stu(s_id)
            elif(choice==4):
                s_id = int(input("Enter student id: "))
                studentName = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                db.update_stu(s_id, studentName, phone)
            elif(choice==5):
                break
            else:
                print("invalid input! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")



if __name__== "__main__":
    main()