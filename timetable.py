# Time Table Creator
import random
def TimeTableCreator(subjects,day_write,final_time_slots):
    day = {}
    subjects_study = random.sample(subjects, k=studyperday)  # subjects that are selected randomly
    day = dict(zip(subjects_study, final_time_slots))
    print(f"{day_write} - {day}")


print("This program generates a time table according to your time preference (morning,afternoon,evening). Subjects are randomly selected but the time slots are fixed so that you get a habit of studying at that particular time.")
subjects = []
while True:
    subject = input("Enter a subject:\n")
    if subject=="":
        break
    subjects.append(subject)
total_hours = int(input("Enter the total number of hours you want to study:\n"))


print("What is your preference of studying: Morning or afternoon or evening:")
time_preference = input()
if time_preference.lower()=="morning":
    time_slots = ["7:00-8:00","8:00-9:00","9:00-10:00","10:00-11:00","2:00-3:00"]
elif time_preference.lower()=="afternoon":
    time_slots = ["12:00-13:00","13:00-14:00","15:00-16:00","16:00-17:00","18:00-19:00"]
elif time_preference.lower()=="evening":
    time_slots = ["16:00-17:00","18:00-19:00","19:00-20:00","20:00-21:00","21:00-22:00"]
else:
    print("Invalid preference")


studyperday = total_hours/7
studyperday = round(studyperday)
print(f"If you want to study {total_hours} in a week then you have to study {studyperday} hours per day.")
final_time_slots = random.sample(time_slots, k=studyperday)  # list of my time slots
print("Here is your required time table\n")

TimeTableCreator(subjects,"Monday",final_time_slots)
TimeTableCreator(subjects,"Tuesday",final_time_slots)
TimeTableCreator(subjects,"Wednesday",final_time_slots)
TimeTableCreator(subjects,"Thursday",final_time_slots)
TimeTableCreator(subjects,"Friday",final_time_slots)
TimeTableCreator(subjects,"Saturday",final_time_slots)
TimeTableCreator(subjects,"Sunday",final_time_slots)


