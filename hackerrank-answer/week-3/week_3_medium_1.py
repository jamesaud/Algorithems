search = ['12', '34']
arr = ['123412',
       '561212',
       '123634',
       '781288']



def inside(search, arr):
    search_len = len(search)
    search_wid = len(search[0])
    arr_len = len(arr)
    arr_wid = len(arr[0])
    for i in range(arr_len - search_len + 1):
        for j in range(arr_wid - search_wid + 1):
            search_row_index = 0
            ii, jj = i, j
            while search_row_index < search_len:
                for num in search[search_row_index]:
                    match = False
                    #print("comparing", arr[ii][jj], num, "in row", arr[ii])
                    if arr[ii][jj] == num:
                        #print(arr[ii][jj], " equals", num, "in row", arr[ii])
                        match = True
                        jj += 1
                    if not match:
                        break;
                    #print()
                if not match:
                    break
                ii += 1
                jj = j
                search_row_index += 1
            if match:
                return 'YES'
    return 'NO'



            
           
print(inside(search, arr))
