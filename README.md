# Route Optimization System

Welcome to the Route Optimization System! This system will help you optimize routes between cities based on different modes of transportation. This guide will help you install and use the system properly.


## Prerequisites

Please install these dependencies first:
+ Python
+ Pyqt5
+ Pyqt5-tools
+ Matplotlib
+ Networkx# Route Optimization System

Welcome to the Route Optimization System! This system will help you optimize routes between cities based on different modes of transportation. This guide will help you install and use the system properly.


## Prerequisites

Please install these dependencies first:
+ Python
+ Pyqt5
+ Pyqt5-tools
+ Matplotlib
+ Networkx

First you need to install python, you can download it from the official site <https://www.python.org/downloads/>
You can install git from the official website <https://git-scm.com/download/win>
You can install rest of the dependencies one by one or by using the following command:
```bash
pip install matplotlib
```

## Starting the system

Open up the terminal run the following commands:
```bash
git clone https://gitlab.com/Mudasir-Ahmad011/dsafinalprojectpid25
cd dsafinalprojectpid25
```
Then you can start the system using:
```bash
python Main.py
```

### User Menu
Upon starting the system, you will be presented with the Sign Up page. Here you can create you account. After creating your account, you can sign in to the system to see the main page. This page consist of two main functions:
1. Visulizing the Complete Map
This option will show the complete map present inside the system.
2. Visulizaing the Shortest Path
You can use the second option by filling the source and destination city and providing a mode of transportation. This will show you the shortest route to your destination, the total distance to that location and the time it would take you to reach that destination.

### Admin Menu
You can also sign in using the admin account to access a different menu.
Default admin is:
Username : AbdulRehman
Password : 12345678
After logging in, you will see all the cities in a tabular form. Here you can perform the following functions:
+ Add User
  You can use this option to add another user or an admin to the system. This is the only way to add an admin.
+ Add City
  You can add another city to the map by providing its information such as its name, coordinates and the adjacent cities.
+ Remove City
  You can also remove an already present city using the option.
+ Sort
  This option will allow you to sort the cities alphabatically.
+ Reload
  To see any change brought by adding or removeing a city, you need to press the reload button present at the top right corner of the table.
