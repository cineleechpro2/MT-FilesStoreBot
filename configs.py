# (c) @MRK_YT

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID","6757518"))
	API_HASH = os.environ.get("API_HASH","110af6ecbf4fe550eb5275d4b242de66")
	BOT_TOKEN = os.environ.get("MT_BOT_TOKEN","2142602714:AAFaaN7aHuaW9Vs_iQw9fRzVFtrxR_If6eY")
	BOT_USERNAME = os.environ.get("MT_BOT_USERNAME","cinesubzfilestorebot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL","-1001229969928"))
	BOT_OWNER = int(os.environ.get("MT_BOT_OWNER","1582275604"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://MRKYT:MRKYT@cluster0.45ehw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("MT_UPDATES_CHANNEL","-1001642247465")
	LOG_CHANNEL = int(os.environ.get("MT_LOG_CHANNEL"," -1001229969928"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("MO_TECH_YT", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍ **Developer:** @AbirHasan2005

👨‍💻 **Editing:** @Mrk_YT

📺 **Support:** [YouTube Channel](https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ)

🗣️ **Any Doubt:** @Mo_Tech_Group

📢 **Updates Channel:** [Discovery Projects](https://t.me/Mo_Tech_YT)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍ **Developer:** @AbirHasan2005

💻 **Developer Details:** [Clcik Here](https://github.com/MoTechYT/MT-FilesStoreBot/blob/main/README.md)

👨‍💻 **Editing:** @Mrk_YT

🗣️ **Any Doubt:** @Mo_Tech_Group

📺 **Support :** [YouTube Channel](https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Mo_Tech_YT)

Donate Now (coming soon)
"""
	HOME_TEXT = """
**👋Hi**, [{}](tg://user?id={})\n\n**CineSubz ❤️ ** **File Share Bot**.

**Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check About Bot Button**.
"""

