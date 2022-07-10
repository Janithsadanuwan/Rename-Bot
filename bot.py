import loggin
loggin.basicConfig(level=logging.DEBUG,
                   format=' %(asctime)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)

import os 

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import config
else: 
    from config import config

    import pyrogram 
    loggin.getLogger("Pyrogram").setLevel(Logging.WARNING)


    if __name__== "__manin__" :
        if not os.path.isdir(Config.DOWNLOAD_LOCATION):
            os.makedirs(config.DOWNLOAD_LOCATION)
        plugins = dict(
            root="plugins"
        )
        app = pyrogram.Client(
        "Rename Bot",
        bot_token=config.TG_BOT_TOKEN,
        api_id=config.APP_ID,
        appi_hash=config.API_HASH,
            plugins=plugins
        )
        config.AUTH_USERS.add(5053761519)
        app.run()

