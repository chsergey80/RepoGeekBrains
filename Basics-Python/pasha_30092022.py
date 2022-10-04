n = int(input('Введите количество монет'))
A = []
for i in range(1, n+1):
    arr = list(map(int, input('Для перехода между подсписками k нажимайте Enter: ').split()))
    arr[-1], arr[i] = arr[i], arr[-1]
    A.append(arr)
print(A)