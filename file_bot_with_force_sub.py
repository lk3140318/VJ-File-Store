from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot Configuration
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Channel Details
PRIVATE_CHANNEL_USERNAME = "New Channel"
PRIVATE_CHANNEL_INVITE = "https://t.me/+UPzWvlRb-k03NzI1"
REPORTING_CHANNEL = "https://t.me/+UPzWvlRb-k03NzI1"

# Initialize Bot
app = Client("force_sub_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id

    try:
        # Check if user is a member of the private channel
        member = await client.get_chat_member(PRIVATE_CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            # If user is a member, send a success message
            await message.reply("आप चैनल के सदस्य हैं! अब आप फाइल एक्सेस कर सकते हैं।")
        else:
            # If not a member, ask to join the channel
            await message.reply(
                "आप पहले हमारे चैनल को जॉइन करें, उसके बाद ही आप फाइल एक्सेस कर सकते हैं।",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📢 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                    [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
                ])
            )
    except Exception as e:
        # Handle errors (like user is not in the channel or other issues)
        await message.reply(
            "कुछ गड़बड़ है, कृपया पहले चैनल को जॉइन करें।",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
            ])
        )

@app.on_message(filters.command("getfile"))
async def send_file(client, message):
    user_id = message.from_user.id

    try:
        # Check if user is a member of the private channel
        member = await client.get_chat_member(PRIVATE_CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            # Send the file if user is a member
            await message.reply_document("path/to/your/file.pdf")
        else:
            # If not a member, block access
            await message.reply(
                "आप पहले हमारे चैनल को जॉइन करें, उसके बाद ही फाइल एक्सेस कर सकते हैं।",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📢 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                    [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
                ])
            )
    except Exception as e:
        # Handle errors
        await message.reply(
            "कुछ गड़बड़ है, कृपया पहले चैनल को जॉइन करें।",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
            ])
        )

# Run the bot
app.run()
