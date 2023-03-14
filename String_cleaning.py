def remove_ws(text):
    return text.replace(" ","").replace("\n","")

def main():
    ip_1="192.20.246.138:\n 6666"
    ip_2= "206.130.99.82:\n8080"

    print(remove_ws(ip_1))
    print(remove_ws(ip_2))




if __name__ == '__main__':
    main()