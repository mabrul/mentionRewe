import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from config import API_ID, API_HASH, TOKEN

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
kntl = TelegramClient('kynan', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


@kntl.on(events.NewMessage(pattern="^/start$"))
async def help(event):
  helptext = "𝘆𝗮𝗲𝗹𝗮𝗵 𝗶𝗱𝗶𝗼𝘁 𝘁𝗶𝗻𝗴𝗴𝗮𝗹 𝗸𝗲𝘁𝗶𝗸 𝗮𝗹𝗹 𝗱𝗼𝗮𝗻𝗴 𝗯𝗲𝗴𝗼 𝗯𝗮𝗻𝗴𝗲𝘁 𝗸𝗹𝗶𝗸 𝗸𝗹𝗶𝗸 𝘀𝘁𝗮𝗿𝘁 𝗺𝗮𝗸 𝗸𝗮𝗺𝘂 𝗸𝗹𝗶𝗸 𝘀𝘁𝗮𝗿𝘁,𝗸𝗮𝗹𝗼 𝗺𝗮𝘂 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝘁𝗶𝗻𝗴𝗴𝗮𝗹 𝗸𝗲𝘁𝗶𝗸 /play (𝗷𝘂𝗱𝘂𝗹 𝗹𝗮𝗴𝘂),𝗸𝗮𝗹𝗼 𝗺𝗮𝘂 𝗽𝗹𝗮𝘆 𝘃𝗶𝗱𝗲𝗼 𝘁𝗶𝗻𝗴𝗴𝗮𝗹 𝗸𝗲𝘁𝗶𝗸 /vplay (𝗷𝘂𝗱𝘂𝗹 𝘃𝗶𝗱𝗲𝗼),𝗸𝗮𝗹𝗼 𝗴𝗮 𝗻𝘆𝗮𝘂𝘁 𝗻𝗴𝗮𝗱𝘂 𝗮𝗷𝗮 𝘀𝗮𝗺𝗮 𝘀𝗲𝘀𝗲𝗽𝘂𝗵 𝘆𝗮𝗻𝗴 𝗱𝗶𝗯𝗮𝘄𝗮𝗵 𝗶𝘁𝘂."
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('Guaa', 't.me/aksaraxzb'),
      ],
      [
        Button.url('Support Gua', 't.me/SupprotRewe'),
        Button.url('Ch Gua', 't.me/aksarabold'),
      ],
    )
  )
  
@kntl.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("𝙟𝙖𝙣𝙜𝙖𝙣 𝙥𝙧𝙞𝙫𝙖𝙩𝙚 𝙞𝙙𝙞𝙤𝙩!")
  
  is_admin = False
  try:
    partici_ = await kntl(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("𝙡𝙪 𝙗𝙪𝙠𝙣 𝙖𝙙𝙢𝙞𝙣 𝙞𝙙𝙞𝙤𝙩 𝙗𝙖𝙣𝙜𝙚𝙩 𝙗𝙤𝙘𝙖𝙝")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("𝙢𝙞𝙣𝙞𝙢𝙖𝙡 𝙠𝙖𝙨𝙞𝙝 𝙥𝙚𝙨𝙖𝙣 𝙞𝙙𝙞𝙤𝙩 𝙗𝙖𝙣𝙜𝙚𝙩!")
  elif event.pattern_match.group(1):
    mode = "teks"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "balas"
    msg = await event.get_reply_message()
    if msg is None:
        return await event.respond("𝙨𝙞 𝙖𝙣𝙟𝙚𝙣𝙜 𝙙𝙞𝙗𝙞𝙡𝙖𝙣𝙜 𝙠𝙖𝙨𝙞 𝙥𝙚𝙨𝙖𝙣 𝙞𝙙𝙞𝙤𝙩 𝙗𝙚𝙩 𝙗𝙤𝙘𝙖𝙝 𝙚𝙩𝙙𝙖𝙝")
  else:
    return await event.respond("𝙨𝙞 𝙖𝙣𝙟𝙚𝙣𝙜 𝙙𝙞𝙗𝙞𝙡𝙖𝙣𝙜 𝙠𝙖𝙨𝙞 𝙥𝙚𝙨𝙖𝙣 𝙞𝙙𝙞𝙤𝙩 𝙗𝙚𝙩 𝙗𝙤𝙘𝙖𝙝 𝙚𝙩𝙙𝙖𝙝")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in kntl.iter_participants(chat_id):
    if not chat_id or chat_id not in spam_chats:
      break
    usrnum += 1
    usrtxt += f"🀄︎ [{usr.first_name}](tg://user?id={usr.id})\n"
    if usrnum == 5:
      if mode == "teks":
        txt = f"{msg}\n\n{usrtxt}"
        await kntl.send_message(chat_id, txt)
      elif mode == "balas":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except Exception as e:
    print(f"Error: {e}")
    pass

@kntl.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id or event.chat_id not in spam_chats:
    return await event.respond('𝙚𝙝 𝙢𝙪𝙠𝙖 𝙖𝙣𝙘𝙪𝙧 𝙤𝙧𝙖𝙣𝙜 𝙜𝙖𝙙𝙖 𝙩𝙖𝙜 𝙖𝙡𝙡 𝙜𝙤𝙗𝙡𝙤𝙠')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except Exception as e:
      print(f"Error: {e}")
      pass
    return await event.respond('𝙞𝙮𝙖 𝙢𝙪𝙠𝙖 𝙖𝙣𝙘𝙪𝙧 𝙣𝙞 𝙜𝙪𝙖 𝙨𝙩𝙤𝙥𝙞𝙣')



print("BOT AKTIF")
kntl.run_until_disconnected()
