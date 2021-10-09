import os, pyautogui, time

APP_FOLDER = 'D:\\Game\Bigo\\bigo account\\BigoaccountShorcutScripts\\BigoaccountShorcut'

totalFiles = 0

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for Files in files:
        totalFiles += 1


for x in range(totalFiles):
    total=(x+1)
    if(total>=100):
        Stringtotal = str(total)
    elif(total>=10):
        Stringtotal = "0" + str(total)
    else:
        Stringtotal = "00" + str(total)
    os.startfile("BigoaccountShorcut\\"+Stringtotal+".lnk")


    def login():
        location = pyautogui.locateCenterOnScreen('loginbutton.png')
        pyautogui.moveTo(location)
        pyautogui.doubleClick(location)
        print(location)
    def google():
        location = pyautogui.locateCenterOnScreen('google3.png')
        pyautogui.moveTo(location)
        pyautogui.doubleClick(location)
        print(location)
    def loginaccount():
        pyautogui.doubleClick(966, 575)
    def close():
        pyautogui.doubleClick(1893, 16)

    login()
    time.sleep(2)
    google()
    time.sleep(2)
    loginaccount()
    time.sleep(10)
    close()

