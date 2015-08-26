from operator import add,sub,div,mul
from random import randint,choice

ops={'+':add,'-':sub,'*':mul,'/':div}
MAXTRIES=2

def doprob():
  op=choice('+-*/')
  if op=='/':
    while True:
      nums=[randint(1,10) for i in range(2)]
      nums.sort(reverse=True)
      if nums[0]%nums[1] == 0:
        break
  else:
    nums=[randint(1,10) for i in range(2)]
    nums.sort(reverse=True)

  ans=ops[op](*nums)
  pr='%d %s %d=' % (nums[0],op,nums[1])
  oops=0
  while True:
    try:
      if int(raw_input(pr))==ans:
        print 'correct'
        break
      if oops==MAXTRIES:
        print 'answer\n%s%d' % (pr,ans)
      else:
        print 'incorrect.try again'
        oops+=1
    except (KeyboardInterrupt,EOFError,ValueError):
      print 'invalid input..try again'

def main():
  while True:
    doprob()
    try:
      opt=raw_input('again?[y/n]').lower()
      if opt and opt[0]=='n':
        break
    except (KeyboardInterrupt,EOFError):
      break

if __name__=='__main__':
  main()
