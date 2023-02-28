from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
		n = int(input())
		nums = []
		for _ in range(n // 10 + 1):
				nums += list(map(int, input().split()))

		print(n // 2 + 1)
		for i in range(1, len(nums) + 1, 2):
						print(sorted(nums[:i])[i // 2], end=' ')
		print()