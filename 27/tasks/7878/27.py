def fileA():
    with open("27A_7878.txt", "r", encoding="utf-8") as file:
        n, k = [int(file.readline()) for _ in range(2)]
        l = [int(file.readline()) for _ in range(n)]
        min_value = float("inf")

        for i in range(n):
            for j in range(i+k, n):
                if abs(i-j) >= k and (l[i]*l[j]) % 157 == 0:
                    min_value = min(min_value, l[i]*l[j])
        print(min_value)


def fileB():
    with open("27A_7878.txt", "r", encoding="utf-8") as file:
        n, k = [int(file.readline()) for _ in range(2)]
        num1 = [0, float("inf")]
        num2 = [0, float("inf")]
        min_value = float("inf")
        print(k)
        for i in range(n):
            num = int(file.readline())
            if num % 157 == 0 and num < num1[1]:
                num1 = [i, num]
            elif num % 157 !=0 and num < num2[1]:
                num2 = [i, num]
            if abs(num1[0]-num2[0]) >= k:
                min_value = min(min_value, num1[1]*num2[1])
        print(min_value)
        print(num1, num2)
fileB()
