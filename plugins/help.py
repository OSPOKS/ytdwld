from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = "Aw le! Youtube Video Mp3/Mp4 engpawh ka download theia, Mahse, Playlists a theih loh thung. Youtube URL Link lo thawn tawp la aw. Chuan Mp3/Mp4 i duh ilo thlang mai ang. Powered by @ZauTe_Km"
    await message.reply_text(helptxt)
