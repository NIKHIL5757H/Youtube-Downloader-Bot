from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/Super_botz")],[InlineKeyboardButton("MY CREATOR", url="https://t.me/NGYNY")],
        [InlineKeyboardButton("Support Group", url="https://t.me/super_botz_support")],[InlineKeyboardButton("REPØRT BUGS", url="https://t.me/NGYNY")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n  \nThis Is YouTube Video Downloader Bot \n  \n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
