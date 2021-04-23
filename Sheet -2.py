n = int(input())
a_cnt = 2 * input().count('A')
print('Friendship' if n == a_cnt else ['Anton', 'Danik'][n > a_cnt])