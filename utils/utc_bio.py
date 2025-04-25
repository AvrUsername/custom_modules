from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
import asyncio
import pytz
import json
import os

from utils.misc import modules_help, prefix

running = False
tz_region = "UTC"
bio_template = "🕒 {time}"
config_file = "userbot_data/utc_bio_config.json"

os.makedirs("userbot_data", exist_ok=True)

def save_config():
    with open(config_file, "w") as f:
        json.dump({"tz": tz_region, "template": bio_template}, f)

def load_config():
    global tz_region, bio_template
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            data = json.load(f)
            tz_region = data.get("tz", "UTC")
            bio_template = data.get("template", "🕒 {time}")

load_config()

def get_clock_emoji(hour):
    clock = {
        0: "🕛", 1: "🕐", 2: "🕑", 3: "🕒", 4: "🕓", 5: "🕔",
        6: "🕕", 7: "🕖", 8: "🕗", 9: "🕘", 10: "🕙", 11: "🕚",
        12: "🕛", 13: "🕐", 14: "🕑", 15: "🕒", 16: "🕓", 17: "🕔",
        18: "🕕", 19: "🕖", 20: "🕗", 21: "🕘", 22: "🕙", 23: "🕚"
    }
    return clock.get(hour % 24, "🕰️")

@Client.on_message(filters.command("setbiozone", prefix) & filters.me)
async def setbiozone(client: Client, message: Message):
    global tz_region
    try:
        zone = message.text.split(" ", 1)[1]
    except IndexError:
        return await message.edit("⛔ Format: `.setbiozone Region/City`")

    if zone not in pytz.all_timezones:
        return await message.edit("⛔ Invalid timezone. Example: `Asia/Tashkent`")

    tz_region = zone
    save_config()
    await message.edit(f"✅ Timezone set to `{tz_region}`")

@Client.on_message(filters.command("setbiotemplate", prefix) & filters.me)
async def setbiotemplate(client: Client, message: Message):
    global bio_template
    try:
        template = message.text.split(" ", 1)[1]
    except IndexError:
        return await message.edit("⛔ Format: `.setbiotemplate {time} | Custom text`")

    if "{time}" not in template:
        return await message.edit("⛔ Template must contain `{time}`")

    bio_template = template
    save_config()
    await message.edit("✅ Bio template saved.")

@Client.on_message(filters.command("startutcbio", prefix) & filters.me)
async def startutcbio(client: Client, message: Message):
    global running
    if running:
        return await message.edit("⏳ Already running.")
    await message.edit(f"✅ Started bio updater. Timezone: `{tz_region}`")

    running = True
    while running:
        try:
            now = datetime.now(pytz.timezone(tz_region))
            time_str = now.strftime("%H:%M %d %B")
            emoji = get_clock_emoji(now.hour)
            new_bio = bio_template.replace("{time}", f"{emoji} {time_str}")
            await client.update_profile(bio=new_bio)
            await asyncio.sleep(60)
        except Exception as e:
            print(f"[UTC_BIO] Error: {e}")
            break

@Client.on_message(filters.command("stoputcbio", prefix) & filters.me)
async def stoputcbio(client: Client, message: Message):
    global running
    running = False
    await message.edit("🛑 Bio updater stopped.")

modules_help["utc_bio"] = {
    "setbiozone [Region/City]": "Set the timezone (e.g. Asia/Tashkent)",
    "setbiotemplate [text with {time}]": "Set bio format. Must include {time}",
    "startutcbio": "Start auto-updating your bio with time",
    "stoputcbio": "Stop updating your bio",
}
