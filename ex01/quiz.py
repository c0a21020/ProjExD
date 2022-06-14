from random import randint

que = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオからみてどんな関係？"]
ans = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]

mondai = randint(0,2)
mondaibun = print(f"問題：{que[mondai]}")

def shutudai():
    return mondaibun,Kaito()
    
def Kaito(urans):
    urans = input("答えるんだ：")
    
    for i in range():
        if urans == ans[mondai][i]:
            print("正解！")
        else:
            print("出直してこい！")
    
    return urans