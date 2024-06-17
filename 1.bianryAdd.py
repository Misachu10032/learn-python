def addBinary( a: str, b: str) -> str:

        # int1 = int(a, 2)
        # int2 = int(b, 2)
        # sum_int = int1 + int2
        # return bin(sum_int)[2:]
        result=""
        i,j=len(a)-1,len(b)-1
        carry=0
        while i >=0 and j>=0:
            temp=int(a[i])+int(b[j])+carry
            curr=temp%2
            carry=temp//2
            print (temp,curr,carry)
            result=str(curr)+result
            print (result)
            print ('\n')
            i -=1
            j -=1
        while i >=0:
            temp=int(a[i])+carry
            curr=temp%2
            carry=temp//2
            result=str(curr)+result
            i -=1
        while j >=0:
            temp=int(b[j])+carry
            curr=temp%2
            carry=temp//2
            result=str(curr)+result
            j -=1
        if carry ==1:
            return "1"+result
        else: return result

a="1010"
b="1011"
print(addBinary(a,b))