def countElements(arr):
    st = set()
    for val in arr:
        st.add(val)
    count = 0

    for i in range(len(arr)):
        if arr[i]+1 in st:
            count+=1
    
    return count

arr = [1,3,2,3,5,0]

print(countElements(arr))