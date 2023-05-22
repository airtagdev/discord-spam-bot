# SPAMM a Discord Spam Bot

**SPAMM is a universaly compatible python script that delivers a powerful punch of spam to any discord server!**
**SPAMM is a very easy to use on replit. Any device that can run a browser can run SPAMM.**
**Great for anoying people you don't like, or just your friends.**

[Visual Studio Instructions](#instructions-for-visual-studio). **(difficult, but local)**

# Instructions for Replit

- Go to https://replit.com/ and run the repl.

- When prompted, enter your message, discord auth code, and discord channel url.
  - To find your auth code, open a browser window, and sign into discord.
  - Navigate to the server that you want to spam and send a message in the text channel that you want to spam in.
  - Open dev tools (inspect element) and navigate to the **Network** tab.
  - Find the value called **messages** and open it.
  - Scroll down and find **authorization**.
  - Copy your auth code (don't share it with anyone else!) and paste it in when prompted and press enter.
  - Copy the **request url** and paste it in when propted and press enter.

- The repl will run and spam the server of your choice :)

# Instructions for Visual Studio

- Install visual studio code from https://code.visualstudio.com
  - Install python from https://www.python.org/downloads/

- Run visual studio code and navigate > extensions and install python.
  - Run python installer (again) and configure pip to be enabled.

- Open **command prompt/terminal** and run:

        pip install requests

- Open visual studio code and go to explorer.
  - Select create folder, add a new folder to any directory, and set it as the project's directory.

- Select the new file button and name the file **spam.py**
  - Navigate back to the repo, open the **spam.py** file, and copy the contents.
  - Navigate to visual studio code and paste the contents in the **spam.py** file.

- Set your message in **your message here** keeping the quotes in place.

- Add your discord authorization code to **your auth code here** and your request url to **your channel request url here**.
  - To find your auth code, open a browser window, and sign into discord.
  - Navigate to the server that you want to spam and send a message in the text channel that you want to spam in.
  - Open dev tools (inspect element) and navigate to the **Network** tab.
  - Find the value called **messages** and open it.
  - Copy the **request url** and paste it in **your channel request url here**.
  - Scroll down and find **authorization**.
  - Copy your auth code (don't share it with anyone else!) and paste it in **your auth code here**.

- Add a timed delay to **your delay here in seconds** (no less than 1).

- Make sure the text channel you selected is open, run the file, and enjoy spam :)

[back to top](#spamm-a-discord-spam-bot)
