from dictionary import dict_add,dict_del,dict_display,dict_check,d
if __name__=="__main__":
    while(True):
        print("1.Add element to Dictionary\n 2.Delete a pair from dictionary\n 3. Display dictionary \n4. Check key availability of dictionary")
        n=int(input("Choose your choice"))
        if n==1:
            key=int(input("Enter a key"))
            value=input("Enter a value")
            result=dict_add(key,value)
            print(result)
        elif n==2:
            key=int(input("Enter a key to be deleted"))
            result=dict_del(key)
            print(result)
        elif n==3:
            result=dict_display()
            if len(d)!=0:
                for k, v in result.items():
                    print(k,v)
            else:
                print("EMPTY")
        elif n==4:
            key=int(input("Enter the key to be search"))
            result=dict_check(key)
            print(result)
        b=input("Do you want to continue? (Give 'yes' to continue else 'no' to exit)")
        if b=='no':
            break
