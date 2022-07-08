from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "15544136"))
API_HASH = getenv("API_HASH", "547e25d6e6693564ebbafe2a56ddb725")
ARQ_API_KEY = "JSJXIX-TKYMOW-QFCRDR-MNIFZA-ARQ"
ARQ_API_URL = "https://arq.hamker.in/"
BOT_TOKEN = getenv("BOT_TOKEN","5529236088:AAFHny36b7XhIN7bH6JF92zdPp7TqAdMh78")
BOT_NAME = getenv("BOT_NAME","Dragon Music")
BOT_USERNAME = getenv("BOT_USERNAME", "DR4G0NMUS1CBOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DRAG0NBOY")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DRAG0N_WORLD")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQBXB0QE6RI6JftZYXDdlB2SwWMH-otwGSuDEX9CmDeMKh4NVcNvjJCLm3U1GfZ_Ufapt9nvOQGTAAW3TJesQGZ8RZytxvs2z_mE4UD8_PYvtpDO1iP41d_Kzroxk7a5dARVILK4M6WmlnssoVGuvmZN-LadEGn9wogaYck6JlxWLaQlYVf_Op6Kf8CtI62M-jVgRVxVLfUiyAg1X3GdjlFopyil34KJrLbAiIf9sdifXuTDAjEzaID_P7HuuLfPiRbb7lBI3Omc42U_LJ7Uy2NF5Kw8P4ilBuuqRiRHrptRy6hnS0tBU1hhmQ_qOoV9oaVMOO7I5OcuEBuaG4r-0t0tAAAAATs3BPIA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1792725669").split()))
