#!/usr/bin/env python
import os

def print_choice(choice_list):
        i = 1
        for elmt in choice_list:
                print(str(i) + ": " + elmt)
                i += 1
        return get_an_action(i)

def get_an_action(size):
        action = 0
        while (action < 1 or action > size):
                try:
                        action = int(raw_input('---> '))
                except ValueError:
                        print("That's not an int!")
        return action

def use_5_ghz():
        print("\n5Ghz?")
        tech = print_choice(['No', 'Yes'])
        if tech == 1:
                return False
        return True

action_list = ["View WIFI (need root)", "Choose SSID (need root)", "Crack Handshake", "Bruteforce SSID (need root)"]

print("\nWhat do you want?")
action = print_choice(action_list)


if action == 1 or action == 2:
        command = "python wifite2/Wifite.py"
        if action == 2:
                essid = raw_input('\nESSID ---> ')
                command += " -e " + essid
        if use_5_ghz():
                command += " -5"
        os.system(command)
elif action == 3:
        print("\nChoose the handskahe")
        handshake_list = []
        for content in os.listdir("hs"):
                #print(content)
                #if os.path.isfile(content):
                handshake_list.append(content)

        handshake = print_choice(handshake_list)
        print("\nChoose the wordlist")
        wordlist_list = []
        for content in os.listdir("wordlists"):
                #if os.path.isfile(content):
                wordlist_list.append(content)

        wordlist = print_choice(wordlist_list)

        os.system("aircrack-ng hs/" + handshake_list[handshake - 1] + " -w wordlists/" + wordlist_list[wordlist - 1])
elif action == 4:
        confirm = 0
        while(confirm != 1):
                print("\nOnly WPA!")
                print("\nESSID?")
                essid = raw_input('---> ')

                print("\nChoose the wordlist")
                wordlist_list = []
                for content in os.listdir("wordlists"):
                        #if os.path.isfile(content):
                        wordlist_list.append(content)
                wordlist = print_choice(wordlist_list)

                print("\nInterface: ")
                interface = raw_input('---> ')

                print("\nConfirm " + essid + " with " + wordlist_list[wordlist-1] + " on " + interface)
                confirm = print_choice(['Yes', 'No'])

        os.system("bash Mjolnir/mjolnir.sh " + essid + " wordlists/" + wordlist_list[wordlist-1] + " " + interface)
