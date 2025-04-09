if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    [2,3,6,6,5]
    maxi=max(arr)
    for i in range(len(arr)):
        if maxi in arr:
            arr.remove(maxi)
    sec_max=max(arr)
    print(sec_max)
