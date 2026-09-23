def print_n(n):
    if n==0:
        return
    print(n)
    print_n(n-1)

a=5
print_n(a)
# n==0 => Is a Base Case
# print_n(n) => Is a Recursive Case
