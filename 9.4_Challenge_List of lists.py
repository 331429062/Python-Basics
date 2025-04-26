universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

tuition = []
enrollment = []

def enrollment_stats(universities):
    
    for i in range(len(universities)): #rows
            enrollment.append(universities[i][1])
            tuition.append(universities[i][2])
    
    return tuition, enrollment

enrollment_stats(universities)

def mean(lst):
    nums = 0
    for num in lst:
        nums += num

    return nums/len(lst)


def median(lst):
    s = sorted(lst)
    med = 0
    mid = len(lst)//2

    if len(s) % 2 == 0:
         med = (s[mid -1] + s[mid])/2
    elif len(s) % 2 != 0:
         med = s[mid]

    return med

Total_Student = sum(enrollment)
Total_Tuition = sum(tuition)

print('*'*30)
print(f"\nTotal Student:   {Total_Student :.2f}")
print(f"Total Tuition:   {Total_Tuition :,}\n\n")
print(f"Student mean:      {mean(enrollment) :.2f}")
print(f"Student median:    {median(enrollment) :,}\n\n")
print(f"Tuition mean:      {mean(tuition) :.2f}")
print(f"Tuition median:    {median(tuition) :,}\n")
print('*'*30)
      