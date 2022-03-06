from sys import stdin

def solve(s):
  ans = None
  # place your code here!
  return ans

def main():
  line = stdin.readline().strip()
  while line[0]!='E':
    print('MEMBER' if solve(line) else 'NON-MEMBER')
    line = stdin.readline().strip()

main()
