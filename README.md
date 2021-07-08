# Braumberg Castle

The first version of the Braumburg Murder Mystery. An adaptation of an in person game for online remote play.

This inital version uses Flask and Flask-SocketIO for handling the web interface and chats.

Done:
- Create a structure to run simultaneous games
- Initiate sockets to do real-time chats
- store chat history in database

Required to do:
- Create database seed for Items
- Create database seed for charachters
- Create a system to 'activate' or 'equip' items that have a passive effect
- Re-do front end a bit to make sure it's response. Currently only works on small screens
- Complete a create-a-game section to generate new game rooms
- Consider how to run a long or short term game
