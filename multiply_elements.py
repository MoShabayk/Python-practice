def product(li):
    result = 1
    for element in li:
        result = result * element

    return result

def main():
    li =[2,3,5,4]
    print(product(li))

    e_li=[]
    print(product(e_li))

if __name__ == '__main__':
      main()



