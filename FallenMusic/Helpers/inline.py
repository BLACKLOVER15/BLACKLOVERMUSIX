# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲💀", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="↻", callback_data="replay_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ],
        [
            InlineKeyboardButton(text="𝗥𝗲𝘀𝘂𝗺𝗲💀", callback_data="resume_cb"),
            InlineKeyboardButton(text="𝗣𝗮𝘂𝘀𝗲💀", callback_data="pause_cb"),
        ], 
        [
            InlineKeyboardButton(text="𝗦𝗸𝗶𝗽💀", callback_data="skip_cb"),
            InlineKeyboardButton(text="𝗘𝗻𝗱💀", callback_data="end_cb"), 
        ], 
        [    
            InlineKeyboardButton(text="𝗕𝗼𝘀𝘀💀", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁💀", url=config.SUPPORT_CHAT),
        ], 
        [
            InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲💀", callback_data="↻ ᴄʟᴏsᴇ ↻"),
        ], 
    ]   
)  

pm_buttons = [
    [
        InlineKeyboardButton(
            text="💀𝗔𝗗𝗗 𝗠𝗘 𝗕𝗔𝗕𝗨💀",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="💀𝗛𝗲𝗹𝗽 & 𝗖𝗼𝗺𝗺𝗮𝗻𝗱💀", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="𝗖𝗵𝗮𝗻𝗻𝗲𝗹💀", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁💀", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="𝗖𝗼𝗱𝗲💀", url="https://t.me/SSC_MAKER_QUIZ"
        ),
        InlineKeyboardButton(text="𝗕𝗼𝘀𝘀💀", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="💀𝗔𝗗𝗗 𝗠𝗘 𝗕𝗔𝗕𝗨💀",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="𝗖𝗵𝗮𝗻𝗻𝗲𝗹💀", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁💀", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="𝗖𝗼𝗱𝗲💀", url="https://t.me/SSC_MAKER_QUIZ"
        ),
        InlineKeyboardButton(text="𝗕𝗼𝘀𝘀💀", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="💀𝗘𝘃𝗲𝗿𝘆𝗼𝗻𝗲💀",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="𝗦𝘂𝗱𝗼💀", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="𝗕𝗼𝘀𝘀💀", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="𝗛𝗼𝗺𝗲💀", callback_data="fallen_home"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲💀", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁💀", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="𝗕𝗼𝘀𝘀💀", callback_data="fallen_help"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲💀", callback_data="close"),
    ],
]
