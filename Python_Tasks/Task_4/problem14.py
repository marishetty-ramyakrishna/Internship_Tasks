# Problem 14: Set .add()
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
stamps = set()

for i in range(n):
    stamps.add(input())

print(len(stamps))