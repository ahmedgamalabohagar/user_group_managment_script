def add_group():
    groupname = input("Enter group name to create : ").strip()
    success, error = run_command(["sudo", "groupadd", groupname])
    if success:
        print(f" '{groupname}' added successfully.")
    else:
        print(f" Error: {error}")


def delete_group():
    groupname = input("Enter groupname to DELETE: ").strip()
    confirm = input(f"Are you sure you want to delete {groupname} ? (y/n): ")
    
    if confirm.lower() == 'y':
        success, error = run_command(["sudo", "groupdel", groupname])
        if success:
            print(f" group '{groupname}' deleted.")
        else:
            print(f" Error: {error}")

def list_groups():
    with open("/etc/group", "r") as f:
        for line in f:
            parts = line.split(":")
            if int(parts[2]) >= 1000 or parts[0] == "wheel" or parts[0] =="sudo":
                print(f"group: {parts[0]} \t ID: {parts[2]} \t members: {parts[3]}")


def modify_group(option,value):
    groupname = input("Enter the group name: ").strip()
    success, error = run_command(["sudo", "groupmod", "-"+option , value , groupname])
    
    if success:
        print(f" Successfully updated {groupname} with option -{option}.")
    else:
        print(f" Error: {error}")
