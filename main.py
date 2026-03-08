from user_manage import *

from group_manage import *


def main():
    if os.getuid() != 0:
        print(" Please run this script with 'sudo'.")
        return

    while True:
        print("\n--- Server User Manager ---")
        print("1. Add User")
        print("2. Modify User")
        print("3. Delete  User")
        print("4. List  Users")
        print("5. add group")
        print("6. modify group")
        print("7. delete group")
        print("8. list groups")
        print("9. disable  User")
        print("10. enable  user")
        print("11. Change user password")
        
        
        choice = input("Select an option: ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
          while True:
            print("Modify User Options : ")
            print("1-Change Home Directory. ")
            print("2-Change Expiration Data. ")
            print("3-Change Primary Group.")
            print("4-Append user to a new group.")
            print("5-change Username. ")
            print("6-change default shell. ")
            print("7-Change User ID. ")
            print("8-exit.")
            option = int(input("select an option : "))
            if option==1:
                path = input("Enter new home directory path: ").strip()
                modify_user("dm", path)
            elif option==2:
                date = input("enter expiration data in this format => yyyy-mm-dd : ").strip()
                modify_user("e",date)
            elif option==3:
                group = input("enter group name : ").strip()
                modify_user("g",group)
            elif option==4:
                group = input("enter group name : ").strip()
                modify_user("aG",group)
            elif option==5:
                new_username=input("enter new username : ").strip()
                modify_user("l",new_username)
            elif option==6:
                default_shell=input("enter path of shell : ").strip()
                modify_user("s",default_shell)
            elif option==7:
                UID = input("enter new user ID : ").strip()
                modify_user("u",UID)
            elif option==8:
                print("exiting...")
                break
            else :
                print("Invalid choice.")
        elif choice == '3':
            delete_user()
        elif choice == '4':
            list_users()
        elif choice=='5':
            add_group()
        elif choice=='6':
          while True:
            print("MODIFY group options : ")
            print("1-Change group name. ")
            print("2-Change group ID. ")
            print("3-exiting ...")
            option = int(input("select option : "))
            if option==1:
                new_name = input("enter new name : ")
                modify_group("n",new_name)
            elif option==2:
                GID=input("enter new group id > 1000 : ")
                modify_group("g",GID)
            elif option==3:
                break
            else:
                print("invalid input !!")

        elif choice=='7':
            delete_group()
        elif choice=='8':
            list_groups()
       
        elif choice=='9':
            modify_user("L","")
        elif choice == '10':
            modify_user("U","")
        elif choice=='11':
            change_user_password()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
