# Linux Server User & Group Manager (CLI)

A powerful, interactive Python Command Line Interface (CLI) tool designed to simplify Linux system administration. This script automates and streamlines common user and group management tasks directly from the terminal.

## 🚀 Features

### User Management
* **Create Users:** Add new users with a home directory and password in one step.
* **Modify Users:** Easily update user attributes including:
  * Home Directory
  * Account Expiration Date
  * Primary and Secondary Groups
  * Username and User ID (UID)
  * Default Shell
* **Delete Users:** Safely remove users and their associated home directories.
* **Manage Access:** Disable (lock) or enable (unlock) user accounts.
* **Password Management:** Securely change user passwords.
* **List Users:** View all regular system users (UID >= 1000).

### Group Management
* **Create Groups:** Add new system groups.
* **Modify Groups:** Change group names or Group IDs (GID).
* **Delete Groups:** Remove existing groups.
* **List Groups:** View custom groups (GID >= 1000) and essential admin groups (like `wheel` or `sudo`).

## 📂 Project Structure

To maintain clean and modular code, the project is divided into three main files:

```text
├── main.py           # The entry point containing the interactive menu loop.
├── users.py          # Module containing all user-related functions.
├── groups.py         # Module containing all group-related functions.
└── README.md         # Project documentation.
```


## 🛠️ Prerequisites

* A **Linux** environment (The script interacts with `/etc/passwd`, `/etc/group`, and uses Linux-specific commands).
* **Python 3.x** installed.
* **Root/Sudo privileges** (Required to execute user and group modifications).

## 💻 Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/ahmedgamalabohagar/user_group_managment_script.git
cd user_group_managment_script
```

2. **Run the script:**
Because this tool manages system files, it must be executed with `sudo`:
```bash
sudo python3 main.py
```

3. **Follow the interactive menu:**
Simply type the number corresponding to the action you want to perform and follow the on-screen prompts.

## ⚠️ Security Warning
This script executes system-level commands (`useradd`, `usermod`, `chpasswd`, etc.) using `subprocess`. Always ensure you are running this in a trusted environment and be careful when deleting users or groups, as data loss can occur.


## 📝 License
This project is open-source and available under the [MIT License](LICENSE).# user_group_managment_script
