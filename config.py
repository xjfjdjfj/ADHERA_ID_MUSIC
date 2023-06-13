import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "26986162"))
API_HASH = os.getenv("API_HASH", "c63fcc05044560910d6f0f6cccec9411")
SESSION = os.getenv("SESSION", "AQCjB39oNSoSViVzktiC5TH3Pcmsix55-5dlpVJdbJ72OwpZOZN_iFh2ENDewYfkcMkQ1GjqCNeFUdFp05QuMQ5Z5JTX1Lmh4jNG8oM3iK1o3lvTZcAukkI_3dZyczrwTm6nd3jWilVEwU3ybKGIkrcG9k7wCZVJxujL6bnicEH32nNrffRvfGM63ei-k0jnTPl52y4fGyPWyT5eBbGUHHR2kLj-opkeDnDnwud0jD2WbO4_TpnuxAizRRKJ5PU8fjKv7GJfadmIGFE7I2vco1GKlZTju-57ekLxfS3S7497fZv-v5TZAJA3B46LS11YHQwPkg3nC2o300GCbo0QaT3xAAAAAUrKF3AA")
HNDLR = os.getenv("HNDLR", "/")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AsadAlexaVCBot"))
call_py = PyTgCalls(bot)
