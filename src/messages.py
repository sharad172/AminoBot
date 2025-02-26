from src.db import PREFIX


system_messages = {
    "help": f"""
[bc]    ╭  .. ♡  𓂃 ʿ ──╮
[bc]▬▬▬▬▬▬ OMEN ◗   𖥻 ⸃⸃ 𖤐⤸₊° 𓂅
[bc]    ╰     ୨  ◞  ✦ ──╯

[ci]Hey there,this Is Omen aka Your Community Companion and Moderator.I am More Happy Yo help You Out.

[ci]© COMMAND CATEGORY ©

[ci]Bot
[ci]Chatmanage
[ci]Fun
[ci]Info

[ci]Note:Send as -fun for command list Of That Particular Category.For Any Query Reach out to my Master At : https://instagram.com/cyberpunk1709?igshid=YmMyMTA2M2Y=

┊     ┊     ┊       ┊   ┊   ˚✩ ⋆｡˚  ✩ °  
┊     ┊     ┊       ┊  .✫ °                        ┊        ⊹  ┊     ┊
┊     ✫.    ┊       ☪︎⋆                            °  ┊           .✫      ┊
┊ ⊹         °┊                                           ☪︎ ⋆                     ┊
☪︎ ⋆.          ┊. ˚                                                                  ˚✩
""",

    "gm": f""" [ic]Very Good Wala Good Morning ๑(◕‿◕)๑""",
    
    "ping": f"""Pong!""",
    
    "info": f"""
[bc]Information

[ci]{PREFIX}get (amino-url)
[c]The object id.

[ci]{PREFIX}chatimages
[c]The сhat's background and icon.

[ci]{PREFIX}media (reply)
[c]Link of image, video or voice message.

[ci]{PREFIX}sticker (reply)
[c]Info about sticker.

[ci]{PREFIX}user [user-link]
[c]info about user.

[ci]{PREFIX}chat [chat-link]
[c]info about chat.

[ci]{PREFIX}com [community-link]
[c]Info about community. (Link - only about open coms)
""",


    "chatmanage": f"""
[bc]Chat management
[ci]{PREFIX}save
[c]Saving the title, description, icon and background of the current chat to the database.
[c](Available only for Host and coHosts)

[ci]{PREFIX}upload
[c]Set the title, description, icon and background from the last save of the current chat.
[c](Available only for Host and coHosts. Bot must have a coHost or Host)

[ci]{PREFIX}mention [message]
[c]Mentions all chat members. (Available only to the Host)

[ci]{PREFIX}block/allow (command)
[c]Blocks/Allow a command in chat.
[c]"{PREFIX}block all" to block all commands.
[c](Available only for Host and coHosts)

[ci]{PREFIX}blockedlist
[c]List of blocked commands.
""",


    "fun": f"""
[BC]Fun
[ci]{PREFIX}8ball
[c]Magic 8 ball answer.

[ci]{PREFIX}a (message)
[c]Chat with chatbot.

[ci]{PREFIX}choice (your-words)
[c]Random word.

[ci]{PREFIX}coin
[c]Tails, heads or edge (0.5%).

[ci]{PREFIX}fancy (text)
[c]Makes the font look nice.

[ci]{PREFIX}kickorg
[c]Prank the chat's Host :).

[ci]{PREFIX}lurk
[c]How many users are watching the chat.

[ci]{PREFIX}mafia (names-of-members)
[c]Distribution of roles for the mafia.
[c](From 3 to 18 people)

[ci]{PREFIX}roll [start] [end] [times]
[c]Random number. The default range is 1 to 100.

[ci]{PREFIX}tr (reply)/(text)
[c]Translate reply message or your message.

[ci]{PREFIX}truth/dare [rating]
[c]Truth or Dare. Rating - pg, pg13, r.

[bci]{PREFIX}duel/rr/casino
[c]Duel/RR/Casino commands.
""",


    "bot": f"""
[bc]Bot
[ci]{PREFIX}help
[c]The help message.

[ci]{PREFIX}ping
[c]Check if the bot is online.

[ci]{PREFIX}follow/unfollow
[c]Subscribe to you <3.

[ci]{PREFIX}joinchat [chat-link]
[c]Joins the chat.
[c](Private - invite bot and send {PREFIX}joinchat)

[ci]{PREFIX}joincom (community-link)
[c]Joins the community.

[ci]{PREFIX}msg (text)[reply][mentions]
[c]Sends your message.

[ci]{PREFIX}report (message)
[c]Send your message to the creator.

[ci]{PREFIX}startvc/endvc
[c]Start/End voice chat.
""",


    "duel": f"""
[bc]Duels
[ci]{PREFIX}duel send (@notify)
[c]Sends a duel to whoever is mentioned.

[ci]{PREFIX}duel yes
[c]Accept duel. Chance to shoot first - 50%.

[ci]{PREFIX}duel no
[c]Cancels the current duel, duel sent to you or sent by you.

[ci]{PREFIX}duel shot
[c]Duel shot. Hit chance - 25%.
""",


    "rr": f"""
[bc]Russian Roulette
[ic]{PREFIX}rr create (room-name)
[c]Сreates room for play.

[ic]{PREFIX}rr join (room-name)
[c]Join to the game room.

[ic]{PREFIX}rr leave
[c]Leave from the game room.

[ic]{PREFIX}rr list
[c]Users in the room.

[ic]{PREFIX}rr kick (@notify)
[c]Kick user from room.
[c](Only to the room owners).

[ic]{PREFIX}rr ban/unban (@notify)
[c]Ban/Unban user from room.
[c](Only to the room owners).

[ic]{PREFIX}rr start/stop
[c]Starts/Stops the game in your room.
[c](Only to the room owners).

[ic]{PREFIX}rr shot
[c]Pistol shot.

[ic]{PREFIX}rr spin
[c]Drum spinning (bullets mixing).
""",
    
    "roulette": f"""
[bc]Casino-roulette
[ci]{PREFIX}casino (bet)
[c]Starts the game and places a bet
[c](bet - number [0; 36], 00
[c]color: red, black, green
[c]divide: odd, even)

[ci]{PREFIX}casino leave
[c]Cancels your bet.
""",
    
    "blackjack": f"""
[bc]BlackJack
[ic]{PREFIX}bj start
[c]Starts a game.

[ic]{PREFIX}bj leave
[c]Stops a game.

[ic]{PREFIX}bj hit/stand
[c]Hit or stand.
""",
    
    "ladder": f"""
[bc]Ladder Game
[ic]{PREFIX}ladder start
[c]Starts the game.

[ic]{PREFIX}ladder stop
[c]Ends the game.

[ic]{PREFIX}ladder field
[c]Shows the field.

[ic]{PREFIX}ladder (Буква)
[c]Move into this cell.
[c]({PREFIX}ladder D)
""",


    "8ball": ('It is certain', 'It is decidedly so', 'Without a doubt', 'Yes — definitely', 'You may rely on it',
              'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Yes',
              'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
              'Don’t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful')

    }
