# WarMailer Ver2.0 by USA-Archer
# This program mails a message to a list of PvPGN players
# Email: archer@usa-archer.com
#
#    Copyright (C) 2015 USA-Archer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#

# USED FOR TCP IP COMMUNICATION
import socket

# USED FOR SLEEP
import time

# USED TO CHECK CWD
import os

# GET CURRENT DIR
CWD = os.getcwd()

# BANNER
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print ''' __          __     _____  __  __          _____ _      ______ _____  
 \ \        / /\   |  __ \|  \/  |   /\   |_   _| |    |  ____|  __ \ 
  \ \  /\  / /  \  | |__) | \  / |  /  \    | | | |    | |__  | |__) |
   \ \/  \/ / /\ \ |  _  /| |\/| | / /\ \   | | | |    |  __| |  _  / 
    \  /\  / ____ \| | \ \| |  | |/ ____ \ _| |_| |____| |____| | \ \ 
     \/  \/_/    \_\_|  \_\_|  |_/_/    \_\_____|______|______|_|  \_\\
                                                  Ver2.0 by USA-Archer         '''
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n") 
print "http://USA-Archer.com/\n"
print "# WarMailer Ver2.0 by USA-Archer"
print "# Email: archer@usa-archer.com"
print "# This program mails a message to a list of PvPGN players"
print "# Edit the mail_to_list.txt file at:\n# %s\\configuration_files\n" % CWD
print "DISCLAIMER: Please do not use in military or secret service organizations or"
print "for illegal purposes.\n"

# HARD CODED VARIABLES
BUFFER_SIZE =  2048
PORT = 6112

# SECONDS TO SLEEP BETWEEN COMMANDS TO EVADE FLOOD DISC
SLEEP_NUMBER = 5

# GET USER SUPPLIED VARS
print "MAILBOT LOGIN INFO\n"

# GET USERNAME OF BOT
while True:

    BOT_USERNAME = (raw_input("Username: "))
    if BOT_USERNAME == '':
        print "\n[!] ERROR: Please enter a valid username.\n"
        continue

    break
# GET PASSWORD OF BOT
while True:

    BOT_PASSWORD = (raw_input("Password: "))
    if BOT_PASSWORD == '':
        print "\n[!] ERROR: Please enter a valid password.\n"
        continue

    break
# GET SERVER
while True:

    SERVER = (raw_input("PvPGN Server Name or IP: "))
    if SERVER == '':
        print "\n[!] ERROR: Please enter a valid server name.\n"
        continue

    break

# GET USERNAME LIST OR PROVIDE username_list.txt, HANDLE ERROR IF NOT FOUND
while True:
    try:
        USERNAME_LIST = (raw_input("List of users to send mail to [username_list.txt]: ") or "username_list.txt")
        # OPEN USERNAME_LIST, STRIP NEW LINES, SAVE AS VARIABLE USERS
        with open("configuration_files/" + USERNAME_LIST, 'r') as USERNAME_LIST:
            USERS = [line.strip() for line in USERNAME_LIST]
    except IOError:
        print "\n[!] ERROR: Could not find '%s'\n" % USERNAME_LIST
        continue
    break

# GET WARMAILER MODE
print '''
WarMailer Modes

[1] SINGLE MESSAGE, MULTIPLE USERS: 
    Mail same message to all users, prompt me to input it.
    
[2] CUSTOM MESSAGES, MULTIPLE USERS: 
    Custom message to each user, in mail_msg_list.txt file, 1 per line.
    
    Example: 
    Line1 in username_list.txt -> User1 in msg_list.txt
    Line2 in username_list.txt -> User2 in msg_list.txt
'''
while True:

    MSG_MODE = (raw_input("Mode: "))
    if MSG_MODE == '':
        print "\n[!] ERROR: Please enter a valid selection.\n"
        continue

    break


##########################################
# WARMAILER MODE 2, SNGLE MSG MULTI USER #
##########################################


if MSG_MODE == '1':
    # GET MSG
    while True:

        MSG = (raw_input("Message to Mail [Max 150chars]: "))
        if SERVER == '':
            print "\n[!] ERROR: Please enter a valid message to mail.\n"
            continue

        break

    # CREATE VARIABLES TO BE USED FOR MATH LATER ON
    NUM_OF_USERS = sum(1 for _ in USERS)
    ORIGINAL_NUM_OF_USERS = NUM_OF_USERS


    ##################################
    # MAIL EACH USER IN LIST THE MSG #
    ##################################
    while True:
        # TRY TO LOG IN
        try:
            # DEFINE SOCKET AS TCP IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # CONNECT TO SERVER
            s.connect((SERVER, 6112))
            # LOG IN: HIT ENTER TO INTERACT WITH THE TERMINAL
            s.send("\r\n")
            # TYPE USERNAME
            s.send(BOT_USERNAME)
            # HIT ENTER TO SEND USERNAME
            s.send("\r\n")
            # TYPE PASSWORD
            s.send(BOT_PASSWORD)
            # HIT ENTER TO SEND PASSWORD
            s.send("\r\n")
            # RECIEVE DATA BACK
            data = s.recv(BUFFER_SIZE)
            data = s.recv(BUFFER_SIZE)

            # IF SERVER SAYS LOGIN FAILED
            if "failed" in data:
                s.close()
                print "\n[!] ERROR: Username/password incorrect. Try again.\n"

                # GET USERNAME AGAIN
                while True:

                    BOT_USERNAME = (raw_input("Username: "))
                    if BOT_USERNAME == '':
                        print "\n[!] ERROR: Please enter a valid username.\n"
                        continue

                    break

                # GET PASSWORD AGAIN
                while True:

                    BOT_PASSWORD = (raw_input("Password: "))
                    if BOT_PASSWORD == '':
                        print "\n[!] ERROR: Please enter a valid password.\n"
                        continue

                    break
                continue

            elif "no bot" in data:
                print "\n[!] ERROR: Server says 'Account has no bot access'\n"
                raw_input("\n\nPress Enter to Continue ...")
                continue

            # IF NO ERROR OCCURRED, EXIT THE 'while True' LOOP
            break

        # IF ERROR OCCURED EITHER WHILE CONNECTING OR RECEVING DATA BACK, DO THIS
        except:

            # PRINT ERROR MESSAGE
            print "\n[!] ERROR: Could not connect to server: %s \nCheck if the server name above is correct and online and try again.\n" % SERVER
            # TRY TO GET EXT_IP, IF FAIL PRINT AS UNKOWN

            # GET SERVER AGAIN
            while True:

                SERVER = (raw_input("PvPGN Server Name or IP: "))
                if SERVER == '':
                    print "\n[!] ERROR: Please enter a valid server name.\n"
                    continue

                break

    print "\nWarMailer: SENDING MAIL\n"

    while NUM_OF_USERS > 0:
        for USER in USERS:
            # TYPE /mail send <username> <message> TO SEND MAIL
            s.send("/mail send %s %s .:Sent by WarMailer:. Download at http://USA-Archer.com/" % (USER, MSG))
            # HIT ENTER TO SEND
            s.send("\r\n")

            # RECIEVE DATA BACK
            data = s.recv(BUFFER_SIZE)

            if "flooding" in data:
                s.close()
                print "\n[!] ERROR: You've been disconnected by the server for flooding."
                print "Try again with a higher number of seconds between attacks"
                raw_input("\n\nPress Enter to exit ...")

                break

            # SLEEP TO EVADE FLOOD DISC
            time.sleep(SLEEP_NUMBER)
            NUM_OF_USERS = NUM_OF_USERS - 1
            CURRENT_USER_NUM = ORIGINAL_NUM_OF_USERS - NUM_OF_USERS
            print "WarMailer: STATUS (%s/%s) SUCCESS! Sent %s: '%s'\n" % (CURRENT_USER_NUM, ORIGINAL_NUM_OF_USERS, USER, MSG)

    s.close()
    print "WarMailer: DONE!\n"
    raw_input("\n\nPress Enter to exit ...")



##########################################
# WARMAILER MODE 2, MULTI MSG MULTI USER #
##########################################


if MSG_MODE == '2':
    # GET MSG LIST OR PROVIDE mail_msg_list.txt, HANDLE ERROR IF NOT FOUND
    while True:
        try:
            MSG_LIST = (raw_input("List of messages to send [msg_list.txt]: ") or "msg_list.txt")
            # OPEN USERNAME_LIST, STRIP NEW LINES, SAVE AS VARIABLE USERS
            with open("configuration_files/" + MSG_LIST, 'r') as MSG_LIST:
                MSGS = [line.strip() for line in MSG_LIST]
        except IOError:
            print "\n[!] ERROR: Could not find '%s'\n" % USERNAME_LIST
            continue
        break

# CREATE VARIABLES TO BE USED FOR MATH LATER ON
NUM_OF_USERS = sum(1 for _ in USERS)
ORIGINAL_NUM_OF_USERS = NUM_OF_USERS


###########################
# MAIL EACH USER EACH MSG #
###########################
while True:
    # TRY TO LOG IN
    try:
        # DEFINE SOCKET AS TCP IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # CONNECT TO SERVER
        s.connect((SERVER, 6112))
        # LOG IN: HIT ENTER TO INTERACT WITH THE TERMINAL
        s.send("\r\n")
        # TYPE USERNAME
        s.send(BOT_USERNAME)
        # HIT ENTER TO SEND USERNAME
        s.send("\r\n")
        # TYPE PASSWORD
        s.send(BOT_PASSWORD)
        # HIT ENTER TO SEND PASSWORD
        s.send("\r\n")
        # RECIEVE DATA BACK
        data = s.recv(BUFFER_SIZE)
        data = s.recv(BUFFER_SIZE)

        # IF SERVER SAYS LOGIN FAILED
        if "failed" in data:
            s.close()
            print "\n[!] ERROR: Username/password incorrect. Try again.\n"

            # GET USERNAME AGAIN
            while True:

                BOT_USERNAME = (raw_input("Username: "))
                if BOT_USERNAME == '':
                    print "\n[!] ERROR: Please enter a valid username.\n"
                    continue

                break

            # GET PASSWORD AGAIN
            while True:

                BOT_PASSWORD = (raw_input("Password: "))
                if BOT_PASSWORD == '':
                    print "\n[!] ERROR: Please enter a valid password.\n"
                    continue

                break
            continue

        elif "no bot" in data:
            print "\n[!] ERROR: Server says 'Account has no bot access'\n"
            raw_input("\n\nPress Enter to Continue ...")
            continue

        # IF NO ERROR OCCURRED, EXIT THE 'while True' LOOP
        break

    # IF ERROR OCCURED EITHER WHILE CONNECTING OR RECEVING DATA BACK, DO THIS
    except:

        # PRINT ERROR MESSAGE
        print "\n[!] ERROR: Could not connect to server: %s \nCheck if the server name above is correct and online and try again.\n" % SERVER
        # TRY TO GET EXT_IP, IF FAIL PRINT AS UNKOWN

        # GET SERVER AGAIN
        while True:

            SERVER = (raw_input("PvPGN Server Name or IP: "))
            if SERVER == '':
                print "\n[!] ERROR: Please enter a valid server name.\n"
                continue

            break

print "\nWarMailer: SENDING MAIL\n"

CURRENT_MSG_NUMBER = 0

while NUM_OF_USERS > 0:
    for USER in USERS:
        # TYPE /mail send <username> <message> TO SEND MAIL
        s.send("/mail send %s %s .:Sent by WarMailer:. Download at http://USA-Archer.com/" % (USER, MSGS[CURRENT_MSG_NUMBER]))
        # HIT ENTER TO SEND
        s.send("\r\n")

        # RECIEVE DATA BACK
        data = s.recv(BUFFER_SIZE)

        if "flooding" in data:
            s.close()
            print "\n[!] ERROR: You've been disconnected by the server for flooding."
            print "Try again with a higher number of seconds between attacks"
            raw_input("\n\nPress Enter to exit ...")

            break

        # SLEEP TO EVADE FLOOD DISC
        time.sleep(SLEEP_NUMBER)
        NUM_OF_USERS = NUM_OF_USERS - 1
        CURRENT_USER_NUM = ORIGINAL_NUM_OF_USERS - NUM_OF_USERS
        print "WarMailer: STATUS (%s/%s) SUCCESS! Sent %s: '%s'\n" % (CURRENT_USER_NUM, ORIGINAL_NUM_OF_USERS, USER, MSGS[CURRENT_MSG_NUMBER])
        
        CURRENT_MSG_NUMBER = CURRENT_MSG_NUMBER + 1

s.close()
print "WarMailer: DONE!\n"
raw_input("\n\nPress Enter to exit ...")
