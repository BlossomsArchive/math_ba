import random
from misskey import Misskey
from atproto import Client, models
import os

f = open("question.txt", "r", encoding='utf-8')
old_file = f.read()
old = old_file.split("\n")
f.close()

x = random.randint(1, 9999)
y = random.randint(1, 9999)

# Misskey
misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
misskey_token = os.environ.get("MISSKEY_TOKEN")
api = Misskey(misskey_address,misskey_token)

# Bluesky
bluesky = Client()
bluesky.login(str(os.environ.get("BLUESKY_MAIL_ADDRESS")),str(os.environ.get("BLUESKY_PASSWORD")))

match random.randint(1, 4):
        case 1:
            post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ old[1] +"\" でした！　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " × :unicode_1d54f_bg_black: = " + str(x * y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            post_text_bs = "前回の答えは\"𝕏 = "+ old[1] +"\" でした！　では次の問題です\n\n𝕏にあてはまる数字を求めよ\n"+str(x) + " × 𝕏 = " + str(x * y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            h = open("question.txt", "w", encoding='utf-8')
            h.write(str(x)+"\n"+str(y)+'\n'+'×'+'\n'+str(x * y)+"\n"+old[1])
            h.close()
            print(post_text)
            api.notes_create(text=post_text)
            bluesky.send_post(post_text_bs)


        case 2:
            post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ old[1] +"\" でした！　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " + :unicode_1d54f_bg_black: = " + str(x + y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            post_text = "前回の答えは\"𝕏 = "+ old[1] +"\" でした！　では次の問題です\n\n𝕏にあてはまる数字を求めよ\n"+str(x) + " + 𝕏 = " + str(x + y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            h = open("question.txt", "w", encoding='utf-8')
            h.write(str(x)+"\n"+str(y)+'\n'+'+'+'\n'+str(x + y)+"\n"+old[1])
            h.close()
            print(post_text)
            api.notes_create(text=post_text)
            bluesky.send_post(post_text_bs)

        case 3:
            post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ old[1] +"\" でした!　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " - :unicode_1d54f_bg_black: = " + str(x - y) +"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            post_text = "前回の答えは\"𝕏 = "+ old[1] +"\" でした!　では次の問題です\n\n𝕏にあてはまる数字を求めよ\n"+str(x) + " - 𝕏 = " + str(x - y) +"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            h = open("question.txt", "w", encoding='utf-8')
            h.write(str(x)+"\n"+str(y)+'\n'+'-'+'\n'+str(x - y)+"\n"+old[1])
            h.close()
            print(post_text)
            api.notes_create(text=post_text)
            bluesky.send_post(post_text_bs)

        case 4:
            post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ old[1] +"\" でした！　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " ÷ :unicode_1d54f_bg_black: = " + str(x / y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            post_text = "前回の答えは\"𝕏 = "+ old[1] +"\" でした！　では次の問題です\n\n𝕏にあてはまる数字を求めよ\n"+str(x) + " ÷ 𝕏 = " + str(x / y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
            h = open("question.txt", "w", encoding='utf-8')
            h.write(str(x)+"\n"+str(y)+'\n'+'÷'+'\n'+str(x / y)+"\n"+old[1])
            h.close()
            print(post_text)
            api.notes_create(text=post_text)
            bluesky.send_post(post_text_bs)


print("--書き込み--")
print("X = "+str(x))
print("y = "+str(y))
print("answer ="+str(x - y))
