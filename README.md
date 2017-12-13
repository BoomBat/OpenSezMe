# OpenSezMe
A simple yet effective password manager.

OpenSez me was a shot at a simplistic password manager. And although there are literally hundreds out there I think this one
shines in just how straightforward it is. Other password managers at first glance can be a little daunting, but this one should make you feel comfortable right away with no exploring necessary.

# Manual:
Compile in your favorite python compiler.
If there are no entries just type in a website, username, and password. Or you can set the Alp, Num, and Spec flags at the bottom. (Alphabet, Numbers, Special Characters) then hit Gen. Pass. to generate a password in the current password field.

To add another hit "New" to clear the fields for your next entry.
Highlight entry and and push "Delete" to remove entry.
Then hit save and your entry will be added to the database list.

# Notes:
The application is constructed with the tkinter, pickle, and random modules and Python3.
It also comes with a proprietary module called passdat.

The database is saved to binary with pickle, and loaded the same.

# Future Development:
In the future I want to implement true entropy instead of sudo random password generation.
Encryption to lock down the database until a master password is entered.
Also a bar to give feedback to the user on how strong their password is.
Mayb clean up the UI or construct it with a different toolkit altogether.

Files: OpenSezMe.py
       passdat.py
       passdb
       
