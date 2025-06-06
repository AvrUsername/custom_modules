#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix
from utils.scripts import import_library

import_library("apksearch")

from apksearch import APKPure, APKMirror, AppTeka, APKCombo, APKFab, APKad, Aptoide


def search_apkmirror(query: str) -> str:
    apkmirror = APKMirror(query)
    result = apkmirror.search_apk()
    if result:
        title, apk_link = result
        return f"APKMirror:\n<b>{title}</b>:{apk_link}"
    return "APKMirror:<code>No results found</code>"


def search_apkpure(query: str) -> str:
    apkpure = APKPure(query)
    result = apkpure.search_apk()
    if result:
        title, apk_link = result
        return f"APKPure:\n<b>{title}</b>:{apk_link}"
    return "APKPure:<code>No results found</code>"


def search_appteka(query: str) -> str:
    appteka = AppTeka(query)
    result = appteka.search_apk()
    if result:
        title, apk_link = result
        return f"AppTeka:\n<b>{title}</b>:{apk_link}"
    return "AppTeka:<code>No results found</code>"


def search_apkcombo(query: str) -> str:
    apkcombo = APKCombo(query)
    result = apkcombo.search_apk()
    if result:
        title, apk_link = result
        return f"APKCombo:\n<b>{title}</b>:{apk_link}"
    return "APKCombo:<code>No results found</code>"


def search_apkfab(query: str) -> str:
    apkfab = APKFab(query)
    result = apkfab.search_apk()
    if result:
        title, apk_link = result
        return f"APKFab:\n<b>{title}</b>:{apk_link}"
    return "APKFab:<code>No results found</code>"


def search_apkad(query: str) -> str:
    apkad = APKad(query)
    result = apkad.search_apk()
    if result:
        title, apk_link = result
        return f"APKad:\n<b>{title}</b>:{apk_link}"
    return "APKad:<code>No results found</code>"


def search_aptoide(query: str) -> str:
    aptoide = Aptoide(query)
    result = aptoide.search_apk()
    if result:
        title, apk_link = result
        return f"Aptoide:\n<b>{title}</b>:{apk_link}"
    return "Aptoide:<code>No results found</code>"


def apksearch(query: str) -> str:
    apkmirror_result = search_apkmirror(query)
    apkpure_result = search_apkpure(query)
    appteka_result = search_appteka(query)
    apkcombo_result = search_apkcombo(query)
    apkfab_result = search_apkfab(query)
    apkad_result = search_apkad(query)
    aptoide_result = search_aptoide(query)
    results = [
        apkmirror_result,
        apkpure_result,
        appteka_result,
        apkcombo_result,
        apkfab_result,
        apkad_result,
        aptoide_result,
    ]
    return "\n\n".join(results)


@Client.on_message(filters.command("apkmirror", prefix) & filters.me)
async def apkmirror(_, message: Message):
    if len(message.command) < 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    result = search_apkmirror(query)
    await message.edit_text(result, disable_web_page_preview=True)


@Client.on_message(filters.command("apkpure", prefix) & filters.me)
async def apkpure(_, message: Message):
    if len(message.command) > 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    result = search_apkpure(query)
    await message.edit_text(result, disable_web_page_preview=True)


@Client.on_message(filters.command("apkcombo", prefix) & filters.me)
async def apkcombo(_, message: Message):
    if len(message.command) > 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    result = search_apkcombo(query)
    await message.edit_text(result, disable_web_page_preview=True)


@Client.on_message(filters.command("apkfab", prefix) & filters.me)
async def apkfab(_, message: Message):
    if len(message.command) > 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    result = search_apkfab(query)
    await message.edit_text(result, disable_web_page_preview=True)


@Client.on_message(filters.command("appteka", prefix) & filters.me)
async def appteka(_, message: Message):
    if len(message.command) > 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    result = search_appteka(query)
    await message.edit_text(result, disable_web_page_preview=True)


@Client.on_message(filters.command("apkad", prefix) & filters.me)
async def appteka(_, message: Message):
    if len(message.command) > 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    result = search_apkad(query)
    await message.edit_text(result, disable_web_page_preview=True)


@Client.on_message(filters.command("aptoide", prefix) & filters.me)
async def appteka(_, message: Message):
    if len(message.command) > 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    result = search_aptoide(query)
    await message.edit_text(result, disable_web_page_preview=True)


@Client.on_message(filters.command("apksearch", prefix) & filters.me)
async def apks(_, message: Message):
    if len(message.command) > 2:
        return await message.edit("<code>No query provided</code>")
    query = message.text.split(maxsplit=1)[1]
    await message.edit("<code>Searching...</code>")
    result = apksearch(query)
    await message.edit_text(result, disable_web_page_preview=True)


modules_help["apksearch"] = {
    "apkmirror [package_name]*": "Search for an apk on apkmirror",
    "apkfab [package_name]*": "Search for an apk on apkfab",
    "appteka [package_name]*": "Search for an apk on appteka",
    "apksearch [package_name]*": "Search for an apk on apksearch",
    "apkpure [package_name]*": "Search for an apk on apkpure",
    "aptoide [package_name]*": "Search for an apk on aptoide",
    "apkad [package_name]*": "Search for an apk on apkad",
    "apksearch [package_name]*": "Search for an apk on all supported sources",
}
