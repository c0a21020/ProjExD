from random import randint #あはは

def main():
    kaitou = shutudai()
    Kaito(urans)

def shutudai():
    que = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオからみてどんな関係？"]
    ans = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]

    mondai = randint(0,2)
    
    return print(f"問題：{que[mondai]}"),ans[mondai]
    
def Kaito(urans):
    urans = input("答えるんだ：")
    
    for i in range():
        if urans == ans[mondai][i]:
            print("正解！")
        else:
            print("出直してこい！")

if __name__ == "__main__":
    main()