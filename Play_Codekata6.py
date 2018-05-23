try:
        v1,v2 = [x for x in input("Enter Two Strings:").split()]
        def isom(v1,v2):
                if(len(v1)!=len(v2)):
                        return False
                d1=[False]*256
                d2=[-1]*256
                for i in range(len(v1)):
                        if(d2[ord(v1[i])]==-1):
                                if(d1[ord(v2[i])]):
                                        return False
                                d1[ord(v2[i])] = True
                                d2[ord(v1[i])] = v2[i]
                        elif(d2[ord(v1[i])]!=v2[i]):
                                return False
                return True
        if(isom(v1,v2)):
                print("yes")
        else:
                print("no")
except:
        print("Invalid Input")
