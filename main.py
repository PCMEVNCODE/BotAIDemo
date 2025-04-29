import discord  
# Cấu hình API Gemini (Hãy thay API key bằng biến môi trường)
from google import genai
# FILE CODE SUB FOR MAIN FILE
# <DEVLOPER> >> DANH DEV
#
#openrouter
#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

# id token for discord bot _>>>
tapi = "MTM2MzE0NTA2NzQ4OTAwNTc1OQ.GU3Nl5.PW-hVPxZfUkZN3PMwQDj27L6X1kw3YIX42LfwU"
#____________________________________________________________________________________________
# CHANNEL_ID >>>>
CH_ID = 1363158722242805841
#____________________________________________________________________________________________
# FREFIX TO READ MESSAGE >>>>
FREFIX = "<<"
#____________________________________________________________________________________________
#api_gemini
a_ge = "AIzaSyCR6laHkZeWHVSiEx5l-vsYa8BfU-Mhseg"
#____________________________________________________________________________________________
# API for deepseek
d_api = "sk-ee28221a8a7c47e2b700879218cce84d"
# Đổi tên biến để tránh xung đột
genai_client = genai.Client(api_key=a_ge)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'>>>Bot started : {self.user}')
        channel = self.get_channel(CH_ID)
        
        if channel is None:
            print(f"Lỗi: Không tìm thấy kênh với ID {CH_ID}.")
            return
        
        await channel.send('<<<----Bot started successfully---->>>')
        await channel.send('<Type starting from:"<< <-enter chat word->" for Bot Ai Demo to start replying>')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith(FREFIX):
            tcmd = message.content[len(FREFIX):].strip()
            
            if len(tcmd) > 0:
                print(f"NPS<{message.author.name}>|ID_NPS<{message.author.id}>|M_NPS<{tcmd}>")
                try:
                    # Sử dụng genai_client thay vì client
                    response = genai_client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=tcmd,
                    )
                    if response:
                        if len(response.text) > 2000:
                            # Chia nhỏ nội dung thành các đoạn nhỏ hơn 2000 ký tự
                            for chunk in [response.text[i:i+2000] for i in range(0, len(response.text), 2000)]:
                                await message.channel.send(chunk)
                        else:
                            await message.channel.send(response.text        )
                        print(f">>Bot answered for <{message.author.name}>")
                    else:
                        await message.channel.send("Bot hiện không có phản hồi nào. Vui lòng nhắn nội dung khác!")
                except Exception as e:
                    print(f"WARNING!: Lỗi khi gọi API Gemini: {e}")
                    await message.channel.send("Đã xảy ra lỗi khi xử lý yêu cầu. Vui lòng liên hệ Dảnh Dev để báo cáo lỗi.")

intents = discord.Intents.default()
intents.message_content = True

# Giữ tên client cho Discord bot
client = MyClient(intents=intents)
client.run(tapi)
