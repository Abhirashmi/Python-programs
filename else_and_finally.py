a=open("abhi.txt")


try:
    f=open("doesnt_exist.txt")

except Exception as  e:
    print(e)

finally:
    print("run this anyway ")
    print("closing a ")
    a.close()
# try:
    # f.close()



print("some important stuffff")



f1 = open("harry.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")

