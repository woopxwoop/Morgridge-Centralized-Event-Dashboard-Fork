import logging
import logging.handlers
from config import TOKEN, DATABASE_NAME
from utils.bot import UPLBot

# Setup logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,
)
# Date format
dt_fmt = '%Y-%m-%d %H:%M:%S'

# Set custom format for logs
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')

# Now set the new format to our handler
handler.setFormatter(formatter)
logger.addHandler(handler)

# Setup bot
bot = UPLBot()

if __name__=='__main__':
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)