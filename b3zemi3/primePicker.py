import math
import time

# def main():
n = input('数字を入力してください: ')
n = int(n)
# if isinstance(n, int):
#     raise TypeError('int型で入力してください')
if n < 2:
    raise ValueError('2以上を入力してください')

time_start = time.time()


prime = [True] * n
prime[0] = False
prime[1] = False

sqrt_n = math.sqrt(n)
floor_n = math.floor(n)

for i in range(2, floor_n):
    if not  prime[i]:
        continue
    # p = 2 * i + 1

    # NOTE: 2 * i (i + 1) == p^2
    # for j in range(2 * i * (i + 1), len(prime), p):
    for j in range(i * i, n, i):
        prime[j] =  False


time_end = time.time()
tim = round(time_end - time_start, 8)
print('{}秒'.format(tim))
# print('hoge{}です'.format([i for i in range(n + 1) is prime[i]]))
prime_count = prime.count(True)
print('{0}以下の素数の個数は{1}です'.format(n, prime_count))

for i in range(1, len(prime)):
    if prime[i] == True:
        print('{}'.format(i))
# prime_file = open('prime.txt', 'w')
# prime_file.writelines(data)
# prime_file.close()
