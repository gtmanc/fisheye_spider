import msvcrt

def pwd_input():    
    chars = []   
    while True:  
        try:  
            newChar = msvcrt.getch().decode(encoding="utf-8")  
        except:  
            return input("你很可能不是在cmd命令行下運行，密碼輸入將不能隱藏:")  
        if newChar in '\r\n': # 如果是換行，則輸入結束               
             break   
        elif newChar == '\b': # 如果是退格，則刪除密碼末尾一位並且刪除一個星號   
             if chars:    
                 del chars[-1]   
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 光標回退一格  
                 msvcrt.putch(' '.encode(encoding='utf-8')) # 輸出一個空格覆蓋原來的星號  
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 光標回退一格準備接受新的輸入                   
        else:  
            chars.append(newChar)  
            msvcrt.putch('*'.encode(encoding='utf-8')) # 顯示為星號  
    return (''.join(chars) )