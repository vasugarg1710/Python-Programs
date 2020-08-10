import random


def get_suffled_subjects(diff_subjects, easy_subjects, count):
    # This exact order of appending is important to get diff and easy subjects in the ratio of 2:1
    subjects_list = diff_subjects + easy_subjects + diff_subjects
    shuffled_list = []
    i = 0
    while True:
        if count == 0:
            break
        shuffled_list.append(subjects_list[i])
        count -= 1
        i += 1
        if i == len(subjects_list):
            i = 0
    random.shuffle(shuffled_list)
    return shuffled_list


def get_time_table_for_week(time_slots, study_hours_per_week, diff_subjects, easy_subjects):
    days_in_week_string = 'Monday Tuesday Wednesday Thurdsay Friday Saturday Sunday'
    days_in_week = days_in_week_string.split(' ')
    remaining_study_hours_in_this_week = study_hours_per_week
    study_hours_per_day_floored = int(study_hours_per_week / len(days_in_week))
    exact_study_hours_by_weekday = {}
    for weekday in days_in_week:
        exact_study_hours_by_weekday[weekday] = study_hours_per_day_floored
    modulo_days = remaining_study_hours_in_this_week - (study_hours_per_day_floored * len(days_in_week))
    for weekday in days_in_week:
        if modulo_days == 0:
            break
        exact_study_hours_by_weekday[weekday] += 1
        modulo_days -= 1
    shuffled_subjects_list = get_suffled_subjects(diff_subjects, easy_subjects, study_hours_per_week)

    week_slot_mapping = {}
    shuffled_subjects_index = 0
    for weekday in days_in_week:
        weekday_hours = exact_study_hours_by_weekday[weekday]
        week_slot_mapping[weekday] = {}
        for i in range(weekday_hours):
            week_slot_mapping[weekday][time_slots[i]] = shuffled_subjects_list[shuffled_subjects_index]
            shuffled_subjects_index += 1
    return week_slot_mapping


def print_welcome():
    print("This program generates a time table according to your time preference (morning,afternoon,evening). Subjects are selected by using difficulty level but the time slots are fixed so that you get a habit of studying at that particular time.")
    print("You can run this program multiple times to select best time table for you")


def get_time_slot_preference():
    time_slots = {}
    time_slots['morning'] = ["7:00-8:00","8:00-9:00","9:00-10:00","10:00-11:00","2:00-3:00"]
    time_slots['afternoon'] = ["12:00-13:00","13:00-14:00","15:00-16:00","16:00-17:00","18:00-19:00"]
    time_slots['evening'] = ["16:00-17:00","18:00-19:00","19:00-20:00","20:00-21:00","21:00-22:00"]
    time_slot_preference = input("What is your preference of studying: 'morning' / 'afternoon' / 'evening':")
    if time_slot_preference not in time_slots:
        print("Invalid time slot preference")
        exit(-1)
    return time_slots[time_slot_preference]


def get_subjects(total_hours_per_week):
    num_max_subjects = total_hours_per_week
    diff_subjects = []
    easy_subjects = []
    diff = input(f"Enter the difficult subjects separated by a space (max {num_max_subjects})\n")
    diff_subjects = diff.split()
    if num_max_subjects - len(diff_subjects) > 0:
        easy = input(f"Enter the easy subjects separated by a space (max {num_max_subjects - len(diff_subjects)})\n")
        easy_subjects = easy.split()
    return diff_subjects, easy_subjects


def main():
    print_welcome()
    preferred_time_slot = get_time_slot_preference()
    NUM_DAYS_IN_WEEK = 7
    max_hours_per_week = len(preferred_time_slot) * NUM_DAYS_IN_WEEK
    study_hours_per_week = int(input(f"Enter the total number of hours you want to study in the whole week (max {max_hours_per_week}):\n"))
    print(f"If you want to study {study_hours_per_week} in a week then you have to study {round(study_hours_per_week / NUM_DAYS_IN_WEEK)} hours per day on average")
    diff_subjects, easy_subjects = get_subjects(study_hours_per_week)

    time_table_for_week = get_time_table_for_week(preferred_time_slot, study_hours_per_week, diff_subjects, easy_subjects)
    print("Here is your required time table\n")

    # time_table_for_week = get_time_table_for_week(["16:00-17:00","18:00-19:00","19:00-20:00","20:00-21:00","21:00-22:00"], 20, ['English'], ['Hindi'])
    for key, value in time_table_for_week.items():
        print(key)
        print(value)


main()