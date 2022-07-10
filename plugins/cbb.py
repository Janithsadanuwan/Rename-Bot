import pyrogram

from plugins.help_txt import rename_cb, cancel_extract
from plugins.rename_file import force_name 


@pyrogram.client.on_callback_query()
async def cb_handler(bot, update):

    if "renmae_button" in update.data:
        await update.message.delte()
        await force_name(bot, update.message)

    elif "cancel_e" in update.data:
            await update.message.delete()
            await cancel_extract(bot, update.message)