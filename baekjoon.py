input_list=[int(i) for i in input().split(' ')]
num_array=[int(i) for i in input().split(' ')]
st=0
en=0
sum=0
min=100001
while st<len(num_array) or en<len(num_array):
    #print(st,en)
    if(en==len(num_array)):
        if(min>en-st and sum>=input_list[1]):
            min=en-st
        sum-=num_array[st]
        st+=1
    elif(sum<input_list[1]):
        sum+=num_array[en]
        en+=1
    elif(sum>=input_list[1]):
        sum-=num_array[st]
        if(min>en-st):
            min=en-st
            #print(st,en)
        st+=1
if(min==100001):
    print(0)
else:
    print(min)