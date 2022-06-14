import random

Kurikaeshi = 5
num_taisho = 10
num_kesson = 2

def main():
    for i in range(Kurikaeshi):
        kaito = mondai()
        kaitou(kaito)

def mondai():#問題を表示する関数
    alp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    mondai = random.sample(alp,10)
    
    print("対象文字：") 
    print(mondai)
    print("表示文字：")
    hyouji = random.sample(mondai,8)
    print(hyouji)
    
    return mondai

def kaitou(seikai):#ユーザーの回答の合否判定をする関数
    urans = int(input("欠損文字はいくつあるでしょうか？："))
    if urans == num_kesson:
        print("CORRECT!!")
    else:
        print("WRONG...")

if __name__ == "__main__":
    main()


