# Time Table Creator
import random
def TimeTableCreator(subjects,day_write,final_time_slots):
    day = {}
    subjects_study = random.sample(subjects, k=studyperday)  # subjects that are selected randomly
    day = dict(zip(subjects_study, final_time_slots))
    print(f"{day_write} - {day}")


print("This program generates a time table according to your time preference (morning,afternoon,evening). Subjects are selected by using difficulty level but the time slots are fixed so that you get a habit of studying at that particular time.")
print("You can run this program multiple times to select best time table for you")
diff = input("Enter the difficult subjects separated by a space\n")
easy = input("Enter the easy subjects separated by a space\n")
diffSubjects = diff.split()
easySubjects = easy.split()
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

TimeTableCreator(diffSubjects,"Monday",final_time_slots)
TimeTableCreator(easySubjects,"Tuesday",final_time_slots)
TimeTableCreator(diffSubjects,"Wednesday",final_time_slots)
TimeTableCreator(diffSubjects,"Thursday",final_time_slots)
TimeTableCreator(diffSubjects,"Friday",final_time_slots)
TimeTableCreator(diffSubjects,"Saturday",final_time_slots)
TimeTableCreator(easySubjects,"Sunday",final_time_slots)


