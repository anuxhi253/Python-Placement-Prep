# 47. Balanced parentheses
def is_balanced(s):
    stack=[]; pairs={')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in "({[": stack.append(ch)
        elif not stack or stack.pop()!=pairs[ch]: return False
    return not stack
print(is_balanced("([]{})"))

# 48. Longest substring without repeating chars
s="abcabcbb"
seen=set(); l=0; res=0
for r,ch in enumerate(s):
    while ch in seen:
        seen.remove(s[l]); l+=1
    seen.add(ch); res=max(res,r-l+1)
print(res)

# 49. Max subarray sum (Kadane)
arr=[-2,1,-3,4,-1,2,1,-5,4]
max_sum=cur=arr[0]
for num in arr[1:]:
    cur=max(num,cur+num)
    max_sum=max(max_sum,cur)
print(max_sum)

# 50. Simple calculator
def calc(a,b,op):
    if op=="+": return a+b
    if op=="-": return a-b
    if op=="*": return a*b
    if op=="/": return a/b
print(calc(10,5,"*"))
