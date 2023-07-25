import random
from misskey import Misskey
import os

f = open("answer.txt", "r")
answer = f.read()
f.close()

x = random.randint(1, 9999)
y = random.randint(1, 9999)

h = open("answer.txt", "w")
h.write(str(y))
h.close()

# Misskey
misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
misskey_token = os.environ.get("MISSKEY_TOKEN")
api = Misskey(misskey_address)
api.token = misskey_token

match random.randint(1, 4):
    case 1:
        post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ answer +"\" でした！　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " × :unicode_1d54f_bg_black: = " + str(x * y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
        print(post_text)
        api.notes_create(text=post_text)
       
    case 2:
        post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ answer +"\" でした！　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " + :unicode_1d54f_bg_black: = " + str(x + y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
        print(post_text)
        api.notes_create(text=post_text)

    case 3:
        post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ answer +"\" でした!　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " - :unicode_1d54f_bg_black: = " + str(x - y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
        print(post_text)
        api.notes_create(text=post_text)


    case 4:
        post_text = "前回の答えは\":unicode_1d54f_bg_black: = "+ answer +"\" でした！　では次の問題です\n\n:unicode_1d54f_bg_black:にあてはまる数字を求めよ\n"+str(x) + " ÷ :unicode_1d54f_bg_black: = " + str(x / y)+"\n\n回答は約1時間後に次の問題と一緒に開示されます"
        print(post_text)
        api.notes_create(text=post_text)

print(":unicode_1d54f_bg_black: = "+str(y))