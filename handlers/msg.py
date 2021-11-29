# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",

f"""
**Untuk menggunakan Bot :
\n**Masukkan Bot** >> @candumusic_bot 
**Masukkan Assisten** >> @robotassistenv2**

**Setting Bot** :

1) Jadikan Bot sebagai **Admin** 
2) Start VCG 
3) Ketik /play (judul lagu) 
""",

f"""
**Berikut perintah yang dapat anda gunakan** :

├ /play: 𝘗𝘭𝘢𝘺 𝘮𝘶𝘴𝘪𝘤 𝘥𝘢𝘳𝘪 𝘺𝘰𝘶𝘵𝘶𝘣𝘦 𝘱𝘦𝘯𝘤𝘢𝘳𝘪𝘢𝘯 𝘱𝘦𝘳𝘵𝘢𝘮𝘢 
├ /play [yt link] : 𝘗𝘭𝘢𝘺 𝘮𝘶𝘴𝘪𝘤 𝘥𝘢𝘳𝘪 𝘭𝘪𝘯𝘬 𝘺𝘰𝘶𝘵𝘶𝘣𝘦 
├ /play [reply ke audio]: 𝘗𝘭𝘢𝘺 𝘮𝘶𝘴𝘪𝘤 𝘥𝘢𝘳𝘪 𝘧𝘪𝘭𝘦
├ /song [judul lagu] : 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘭𝘢𝘨𝘶
├══════════════════════════════
├ /player : 𝘔𝘦𝘮𝘣𝘶𝘬𝘢 𝘴𝘦𝘵𝘵𝘪𝘯𝘨 𝘮𝘶𝘴𝘪𝘤
├ /skip : 𝘚𝘬𝘪𝘱 𝘬𝘦 𝘮𝘶𝘴𝘪𝘤 𝘣𝘦𝘳𝘪𝘬𝘶𝘵𝘯𝘺𝘢
├ /pause : 𝘔𝘦𝘯𝘨𝘩𝘦𝘯𝘵𝘪𝘬𝘢𝘯 𝘮𝘶𝘴𝘪𝘤 𝘴𝘦𝘮𝘦𝘯𝘵𝘢𝘳𝘢
├ /resume : 𝘔𝘦𝘭𝘢𝘯𝘫𝘶𝘵𝘬𝘢𝘯 𝘮𝘶𝘴𝘪𝘤
├ /end : 𝘔𝘦𝘯𝘨𝘩𝘦𝘯𝘵𝘪𝘬𝘢𝘯 𝘮𝘶𝘴𝘪𝘤
├ /current : 𝘔𝘦𝘭𝘪𝘩𝘢𝘵 𝘮𝘶𝘴𝘪𝘤 𝘺𝘢𝘯𝘨 𝘴𝘦𝘥𝘢𝘯𝘨 𝘥𝘪𝘮𝘢𝘪𝘯𝘬𝘢𝘯
├ /playlist : 𝘔𝘦𝘭𝘪𝘩𝘢𝘵 𝘥𝘢𝘧𝘵𝘢𝘳 𝘢𝘯𝘵𝘳𝘪𝘢𝘯
├══════════════════════════════
├ /admincache : 𝘙𝘦𝘧𝘳𝘦𝘴𝘩 𝘈𝘥𝘮𝘪𝘯 𝘎𝘳𝘶𝘣
├ /userbotjoin : 𝘐𝘯𝘷𝘪𝘵𝘦 𝘈𝘴𝘴𝘪𝘴𝘵𝘦𝘯 𝘖𝘵𝘰𝘮𝘢𝘵𝘪𝘴
├ /reload : 𝘙𝘦𝘭𝘰𝘢𝘥 𝘈𝘥𝘮𝘪𝘯
""", 
            
f"""
🎶 Saya 𝐂𝐚𝐧𝐝𝐮𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭 👏
Saya akan membantumu **memutar music** di Telegram Groups & Channel, dengan **fitur-fitur** yang menarik.
\n❗ Ketik /help untuk **panduan pemakaiannya**.
❗ Ketik /start untuk **memuat ulang**.
\n───────────────────────────────────
\n_Semua orang pasti mati, tapi tidak semua orang dapat memberi arti. Pastikan hidupmu berarti/bermanfaat untuk orang lain_
\n───────────────────────────────────
\n❃ **Creator : [OWNER](https://t.me/justthetech)
❃ Support dengan doa aja guys! Thanks!
❃ NB : Maaf jika ada kekurangan didalam bot ini**
""",
      ]
