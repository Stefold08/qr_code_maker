import qrcode

while True:
    print("\n ---QR CODE MAKER----")
    print("1. link or text")
    print("2. contact card")
    print("3. wifi")
    print("0. exit")
    choice = input("choose: ")
    
    if choice == "1":
        text = input("Enter link or text: ")
        file = input("File name: ")
        img = qrcode.make(text)
        img.save(file + ".png")
        print("saved ", file + ".png")
        
    elif choice == "2":
        first = input("enter firstname: ")
        last = input("enter lastname: ")
        phone = input("enter phone no. : ")
        email = input("enter email: ")
        
        full = first + " " + last
        card =["Begin:Vcard", "VErsion5.0"]
        card.append("N: " + last + ";" + first)
        card.append("FN: " + full)
        card.append("TEL" + phone)
        card.append("Email" + email)
        card.append("END:VCARD")
        vcard = "\n".join(card)
        
        img = qrcode.make(vcard)
        img.save("contact_qr.png")
        print("saved: contact_qr.png")
        
    elif choice == "3":
        ssid = input("wifi name: ")
        psw = input("WiFi password: ")
        
        wifi = "WIFI:T:WPA;s: " + ssid
        wifi = wifi + ";p:" + psw + ";;"
        
        img = qrcode.make(wifi)
        img.save("wifi_qr.png")
        print("saved")
        
    elif choice == "0":
        print("bye bye")
        break
    else: 
        print("Wrong choice!")
        
        
        
        
        
        