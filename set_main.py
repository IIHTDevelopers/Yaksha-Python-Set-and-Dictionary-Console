from set_operations import set_operations
if __name__=="__main__":
    while(True):
        A={1,2,3,4}
        B={2,10,4,20}
        C={4,10,40,30,2}
        print("1:Union 2:Intersection 3:Difference 4: Symmetric Difference")
        choice=int(input("Enter your choice"))
        result=set_operations(choice,A,B,C)
        print(result)
        b=input("Do you want to continue? (Give 'yes' to continue else 'no' to exit)")
        if b=='no':
            break
