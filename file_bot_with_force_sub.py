from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# बॉट सेटअप
app = Client("file_store_bot", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH", bot_token="YOUR_BOT_TOKEN")

# प्राइवेट चैनल का इन्वाइट लिंक
PRIVATE_CHANNEL_INVITE = "https://t.me/+UPzWvlRb-k03NzI1"

# रिपोर्टिंग चैनल का लिंक (अगर उपयोगकर्ता जॉइन नहीं करता)
REPORTING_CHANNEL = "https://t.me/+UPzWvlRb-k03NzI1"

@app.on_message(filters.command("start"))
async def start_command(client, message):
    try:
        # उपयोगकर्ता की प्राइवेट चैनल में सदस्यता की जांच करें
        user_status = await client.get_chat_member("@your_private_channel_username", message.from_user.id)
        if user_status.status not in ["member", "administrator", "creator"]:
            # अगर उपयोगकर्ता प्राइवेट चैनल का सदस्य नहीं है
            await message.reply_text(
                "आप पहले हमारे प्राइवेट चैनल को जॉइन करें, उसके बाद आप फाइल एक्सेस कर सकते हैं।",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🔒 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                        [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
                    ]
                )
            )
            return
    except:
        # अगर उपयोगकर्ता प्राइवेट चैनल का सदस्य नहीं है या जांच में समस्या है
        await message.reply_text(
            "आप पहले हमारे प्राइवेट चैनल को जॉइन करें, उसके बाद आप फाइल एक्सेस कर सकते हैं।",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔒 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                    [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
                ]
            )
        )
        return

    # अगर उपयोगकर्ता सदस्य है
    await message.reply_text("स्वागत है! आप फाइल एक्सेस कर सकते हैं।")

@app.on_message(filters.command("file"))
async def send_file(client, message):
    try:
        # सदस्यता की जांच करें
        user_status = await client.get_chat_member("@your_private_channel_username", message.from_user.id)
        if user_status.status not in ["member", "administrator", "creator"]:
            await message.reply_text(
                "आप पहले हमारे प्राइवेट चैनल को जॉइन करें, उसके बाद आप फाइल एक्सेस कर सकते हैं।",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🔒 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                        [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
                    ]
                )
            )
            return
    except:
        await message.reply_text(
            "आप पहले हमारे प्राइवेट चैनल को जॉइन करें, उसके बाद आप फाइल एक्सेस कर सकते हैं।",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔒 प्राइवेट चैनल जॉइन करें", url=PRIVATE_CHANNEL_INVITE)],
                    [InlineKeyboardButton("⚠️ रिपोर्ट चैनल", url=REPORTING_CHANNEL)]
                ]
            )
        )
        return

    # फाइल भेजें (फाइल का पथ बदलें)
    await message.reply_document("path/to/your/file")

app.run()
