import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "5204315005:AAFTcY_4CtLVdbN1d-NtQN752dRIdLUKIIA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgAnIp5ZkrC-pm72xC3GwFJBWhUBCJ4mOcrVD1nv7iu_Cc26u38jrrKWcr4XIVtuqmm0zFLBTaSgWkHwdCsDYUea-rZbCZmpMPIyE29fi2TWnYxjCd8L9pAYvQH5i-1qVb2SIOFGd6G7u2v-iapUHkyksF0EHnFG4m0SD_o2RjWEpSACJfwtQOwFJlzuzDeeZf_qjesW-K4fFLY9IUoyhu2kutTZwvkvPBhu_OUChPV_B-hAvj4C1kkjwQ9qt6z4efY3R4QMfvj_jtNounC0yMhFWtqgpmAIEKKh3LArPLMwxaa8cxGnlQpBf_CBBvWGRDtQ-aGGhrUbbpNoDPVXhZDUAAAAAXa9ejgA")
BOT_USERNAME = getenv("BOT_USERNAME", "Saiadjabot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1854384004").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "xl444")
GROUP = getenv("GROUP", "xl444")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/ff43de16d318f461088c7.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/ff43de16d318f461088c7.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/ff43de16d318f461088c7.png") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/ff43de16d318f461088c7.png")

aiohttpsession = aiohttp.ClientSession()


