import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def add_user():
    username = input("Enter the new username: ").strip()
    password = input(f"Enter password for {username}: ").strip()
    
    success, error = run_command(["sudo", "useradd", "-m", username])
    
    if success:
        proc = subprocess.Popen(['sudo', 'chpasswd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        proc.communicate(input=f"{username}:{password}")
        print(f" User '{username}' created successfully.")
    else:
        print(f" Error: {error}")

def list_users():
    print("\n--- System Users (UID >= 1000) ---")
    with open("/etc/passwd", "r") as f:
        for line in f:
            parts = line.split(":")
            if int(parts[2]) >= 1000 and parts[0] != "nobody":
                print(f"User: {parts[0]} \t ID: {parts[2]} \t Home: {parts[5]}")

def delete_user():
    username = input("Enter username to DELETE: ").strip()
    confirm = input(f"Are you sure you want to delete {username} and their files? (y/n): ")
    
    if confirm.lower() == 'y':
        success, error = run_command(["sudo", "userdel", "-r", username])
        if success:
            print(f" User '{username}' deleted.")
        else:
            print(f" Error: {error}")

def modify_user(option,value):
    username = input("Enter the username: ").strip()
    cmd = ["sudo", "usermod", "-" + option]
    if value:
        cmd.append(value)
    cmd.append(username)
    success, error = run_command(cmd)
    if success:
        print(f" Successfully updated {username} with option -{option}.")
    else:
        print(f" Error: {error}")

def change_user_password():
    username = input("Enter the username: ").strip()
    new_password = input(f"Enter NEW password for {username}: ").strip()

    command = ['sudo', 'chpasswd']
    
    try:
        proc = subprocess.Popen(
            command, 
            stdin=subprocess.PIPE,  
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True               
        )
        stdout, stderr = proc.communicate(input=f"{username}:{new_password}")
        if proc.returncode == 0:
            print(f" Password for '{username}' changed successfully.")
        else:
            print(f" Failed to change password. Error: {stderr}")

    except FileNotFoundError:
        print(" Error: The 'chpasswd' command was not found.")
    except PermissionError:
        print(" Error: You need 'sudo' privileges to run this.")

