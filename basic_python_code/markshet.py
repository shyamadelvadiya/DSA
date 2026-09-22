#4.5
maths=90
science=90
ss=96
english=94
gujrati=81

total=maths+science+ss+english+gujrati;
print(total);

per=total/500 *100
print(per)

if(per > 80):
    print("A gread")
elif(per > 60):
    print("B gread")
elif(per > 40):
    print("C grade")
elif(per < 30 ):
    print("Fail")
