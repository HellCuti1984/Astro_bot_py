from environs import Env

# 629766125
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ASTRO_TOKEN = env.str("ASTRO_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
