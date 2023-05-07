#!/usr/bin/env python3
"""
Automated Vulnerability Scanning Script

This script performs regular vulnerability scans of Kubernetes clusters and their components using Aqua or Falco.

Author: Your Name Here
Last Modified: Today's Date Here
"""

import os
import subprocess
import sys


def clear_screen():
    """Clears the terminal screen."""
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")


def run_vulnerability_scan(tool: str):
    """Runs a vulnerability scan using the specified security tool."""
    try:
        subprocess.run([tool, "scan", "--target=kubernetes", "--output-file=vulnerability_report.txt"], check=True)
        print(f"\nVulnerability scan completed using {tool}.")
    except subprocess.CalledProcessError:
        print(f"\nError: Unable to run vulnerability scan using {tool}.")
        sys.exit(1)


def display_menu():
    """Displays the main menu."""
    clear_screen()
    print("Automated Vulnerability Scanning Script\n")
    print("1. Run vulnerability scan using Aqua")
    print("2. Run vulnerability scan using Falco")
    print("3. Exit\n")


def main():
    """Main function that runs the vulnerability scanning script."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            run_vulnerability_scan("aqua")
        elif choice == "2":
            run_vulnerability_scan("falco")
        elif choice == "3":
            print("\nExiting script. Goodbye!\n")
            sys.exit(0)
        else:
            input("\nInvalid choice. Press Enter to try again.")
            continue


if __name__ == "__main__":
    main()

"""
DISCLAIMER:
This script is provided "AS IS" without any warranties of any kind, including without limitation the warranties of merchantability,
fitness for a particular purpose, and non-infringement. The author and contributors assume no responsibility for errors or
omissions in the contents of this script. In no event shall the author and contributors be liable for any damages arising out of
the use of this script.
"""
#This script includes a clear_screen() function that works on both Windows and Linux systems, and it uses subprocess.run() with check=True to raise a CalledProcessError if the command fails to execute properly.

#The script includes a display_menu() function that shows the main menu to the user, and a main() function that repeatedly displays the menu until the user chooses to exit the script.

#The script also includes a disclaimer that specifies that the script is provided "AS IS" without any warranties of any kind, and that the author and contributors assume no responsibility for errors or omissions in the contents of the script.
