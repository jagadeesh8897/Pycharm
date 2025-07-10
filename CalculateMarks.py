lis=list(map(int,input("Enter Marks: ").split()))
def calculate_average(li):
    return sum(li)/len(li)

grade=calculate_average(lis)
def get_grade(li):
    if grade>=90:
        return "A+"
    elif grade>=80 and grade<=89:
        return "A"
    elif grade>=70 and grade<=79:
        return "B"
    elif grade>=60 and grade<=69:
        return "C"
    elif grade>=50 and grade<=59:
        return "D"
    else:
        return "F"

def validate_marks(li):
    if all(li)<=100 and all(li)>=0:
        return True
    return False
print("Average: ",calculate_average(lis))
print("Grade:",get_grade(lis))
print(validate_marks(lis))
