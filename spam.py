import pyautogui, pyperclip, time, random
print("\n  Tool Spam message Đậu Đậu ")
msg = input("  Nhập nội dung cần spam: ").split(" , ")
n = int(input("  Nhập số lần cần spam: "))
m = float(input("  Nhập thời gian chờ gửi tin tiếp theo (giây): "))

print("\n  Chuẩn bị đếm ngược")
for i in range(5,0,-1):
    print(i,end=" ",flush=True)
    time.sleep(1)
print("\n  Bắt đầu")

for j in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(m) #Delay
