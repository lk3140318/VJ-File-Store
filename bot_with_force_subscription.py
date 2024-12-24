from pyrogram import Client, filters

# बॉट सेटअप
app = Client("file_store_bot", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH", bot_token="YOUR_BOT_TOKEN")

# चैनल ID (रिपोर्टिंग चैनल का username या ID)
FORCE_SUB_CHANNEL = "@your_channel_username"

@app.on_message(filters.command(["start"]))
async def start_command(client, message):
    # उपयोगकर्ता चैनल में है या नहीं यह जांचें
    try:
        user_status = await client.get_chat_member(FORCE_SUB_CHANNEL, message.from_user.id)
        if user_status.status not in ["member", "administrator", "creator"]:
            await message.reply_text(
                f"आप पहले {FORCE_SUB_CHANNEL} को जॉइन करें, उसके बाद फाइल एक्सेस करें।"
            )
            return
    except:
        await message.reply_text(
            f"आप पहले {FORCE_SUB_CHANNEL} को जॉइन करें, उसके बाद फाइल एक्सेस करें।"
        )
        return

    # अगर उपयोगकर्ता चैनल में है
    await message.reply_text("आप फाइल एक्सेस कर सकते हैं।")

@app.on_message(filters.command(["file"]))
async def send_file(client, message):
    try:
        user_status = await client.get_chat_member(FORCE_SUB_CHANNEL, message.from_user.id)
        if user_status.status not in ["member", "administrator", "creator"]:
            await message.reply_text(
                f"आप पहले {FORCE_SUB_CHANNEL} को जॉइन करें, उसके बाद फाइल एक्सेस करें।"
            )
            return
    except:
        await message.reply_text(
            f"आप पहले {FORCE_SUB_CHANNEL} को जॉइन करें, उसके बाद फाइल एक्सेस करें।"
        )
        return

    # फाइल भेजें
    await message.reply_document("path/to/your/file")

app.run()
