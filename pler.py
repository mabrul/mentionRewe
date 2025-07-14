import asyncio
import logging
from telethon import TelegramClient, events, Button
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
from config import API_ID, API_HASH, TOKEN


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


bot = TelegramClient("kynan", API_ID, API_HASH).start(bot_token=TOKEN)
spam_chats = set()


@bot.on(events.NewMessage(pattern="^/start$"))
async def start_handler(event):
    msg = (
        "𝘆𝗮𝗲𝗹𝗮𝗵 𝗶𝗱𝗶𝗼𝘁 𝘁𝗶𝗻𝗴𝗴𝗮𝗹 𝗸𝗲𝘁𝗶𝗸 /all 𝗱𝗼𝗮𝗻𝗴 𝗯𝗲𝗴𝗼...\n"
        "𝗻𝗴𝗴𝗮 𝗻𝘆𝗮𝘂𝘁? 𝗹𝗮𝗽𝗼𝗿 𝗸𝗲 𝘀𝗲𝘀𝗲𝗽𝘂𝗵 👇"
    )
    await event.reply(
        msg,
        link_preview=False,
        buttons=[
            [Button.url("Dev 👨‍💻", "https://t.me/LuciferReborns")],
            [
                Button.url("Support Gua", "https://t.me/SupprotRewe"),
                Button.url("Ch Gua", "https://t.me/aksarabold"),
            ]
        ]
    )


@bot.on(events.NewMessage(pattern=r"^/all(?: |$)(.*)"))
async def mention_all_handler(event):
    if event.is_private:
        return await event.respond("𝗷𝗮𝗻𝗴𝗮𝗻 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗯𝗮𝗻𝗴 🗿")

    try:
        participant = await bot(GetParticipantRequest(event.chat_id, event.sender_id))
        is_admin = isinstance(participant.participant, (ChannelParticipantAdmin, ChannelParticipantCreator))
    except UserNotParticipantError:
        is_admin = False

    if not is_admin:
        return await event.respond("𝗟𝘂 𝗯𝘂𝗸𝗮𝗻 𝗮𝗱𝗺𝗶𝗻 𝗯𝗮𝗻𝗴")

    msg_text = event.pattern_match.group(1)
    message_text = None

    if msg_text:
        message_text = msg_text
    elif event.is_reply:
        replied = await event.get_reply_message()
        if replied and replied.text:
            message_text = replied.text
        else:
            return await event.respond("𝗣𝗲𝘀𝗮𝗻 𝗯𝗮𝗹𝗮𝘀𝗮𝗻𝗻𝘆𝗮 𝗴𝗮 𝗮𝗱𝗮 𝘁𝗲𝘅𝘁 𝗯𝗮𝗻𝗴")
    else:
        return await event.respond("𝗠𝗶𝗻𝗶𝗺𝗮𝗹 𝗸𝗮𝘀𝗶𝗵 𝗽𝗲𝘀𝗮𝗻 𝗮𝘁𝗮𝘂 𝗯𝗮𝗹𝗮𝘀 𝗽𝗲𝘀𝗮𝗻")

    spam_chats.add(event.chat_id)
    user_count = 0
    mention_text = ""

    async for user in bot.iter_participants(event.chat_id):
        if event.chat_id not in spam_chats:
            break
        user_count += 1
        mention_text += f"🀄︎ [{user.first_name}](tg://user?id={user.id})\n"
        if user_count == 5:
            try:
                await event.respond(f"{message_text}\n\n{mention_text}")
            except Exception as err:
                LOGGER.error(f"Failed to send message: {err}")
            await asyncio.sleep(2)
            user_count = 0
            mention_text = ""

    spam_chats.discard(event.chat_id)


@bot.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_handler(event):
    if event.chat_id in spam_chats:
        spam_chats.discard(event.chat_id)
        return await event.respond("𝗢𝗞𝗘 𝗕𝗔𝗡𝗚 𝗧𝗔𝗚𝗚𝗡𝗬𝗔 𝗚𝗨𝗔 𝗦𝗧𝗢𝗣𝗜𝗡 🛑")
    return await event.respond("𝗚𝗔𝗞 𝗔𝗗𝗔 𝗧𝗔𝗚𝗚𝗔𝗡 𝗟𝗔𝗚𝗜 𝗡𝗚𝗔𝗣 💤")


if __name__ == "__main__":
    LOGGER.info("Bot aktif dan siap dijalankan...")
    bot.run_until_disconnected()
