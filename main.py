import os
import webbrowser
from pathlib import Path

# Folder this script lives in, so the html file is found no matter
# where main.py is run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, "toolvault.html")

print("===================================")
print(" INVENTORY & TOOL MANAGEMENT ")
print("===================================")

print("1. Tool Management")
print("2. Report")
print("3. Launch Web Interface")
print("4. Exit")

choice = input("Enter Choice: ")

if choice == "1":

    import tool

elif choice == "2":

    import report

elif choice == "3":

    if os.path.exists(HTML_PATH):

        webbrowser.open(Path(HTML_PATH).as_uri())
        print("Opening ToolVault in your browser...")

    else:

        print("toolvault.html not found. Place it in the same folder as main.py")

elif choice == "4":

    print("Program Closed")

else:

    print("Invalid Choice")