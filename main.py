import numpy as np
import random
from tabulate import tabulate

subjects = ["ქართული", "მათემატიკა", "ინგლისური", "ფიზიკა", "ქიმია"]


def generate_random_name():
    first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ',
                   'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა',
                   'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი',
                   'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა', 'ნინელი',
                   'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']
    last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური',
                  'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა',
                  'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია',
                  'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი',
                  'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე',
                  'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე', 'ბერაძე',
                  'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']
    return "{} {}".format(random.choice(first_names), random.choice(last_names))


number_of_students = 100
students = [generate_random_name() for _ in range(number_of_students)]
table = np.random.randint(0, 101, size=(100, 5))


def student_with_highest_avg():
    average_points = np.mean(table, axis=1)
    max_average = np.max(average_points)
    indices = np.where(average_points == max_average)[0]
    return "სტუდენტი/ები ყველაზე მაღალი საშუალო ქულით: " + str([students[i] for i in indices])


def calculate_index(subject, ls):
    index = 0
    for i in ls:
        if i == subject:
            break
        index += 1
    return index


def extremum_score_in_subject(subject, switch):
    index = calculate_index(subject, subjects)

    points = table[:, index]
    if switch == 1:
        max_points = np.max(points)
        indices = np.where(points == max_points)[0]
    else:
        min_points = np.min(points)
        indices = np.where(points == min_points)[0]
    return [students[i] for i in indices]


def highest_score_in_subject(subject):
    return ("ყველაზე მაღალი ქულის მქონე სტუდენტი/ები საგანში - {}: {}"
            .format(subject, extremum_score_in_subject(subject, 1)))


def lowest_score_in_subject(subject):
    return ("ყველაზე დაბალი ქულის მქონე სტუდენტი/ები საგანში - {}: {}"
            .format(subject, extremum_score_in_subject(subject, 0)))


def more_or_less_than_average(subject, switch):
    index = calculate_index(subject, subjects)
    points = table[:, index]
    average = np.mean(points)
    if switch == 1:
        return (f"სტუდენტები საშუალოზე მაღალი ქულით საგანში - {subject}: "
                + str([f"{students[i]}" for i, j in enumerate(points) if j >= average]))
    else:
        return (f"სტუდენტები საშუალოზე დაბალი ქულით საგანში - {subject}: "
                + str([f"{students[i]}" for i, j in enumerate(points) if j < average]))


def more_than_average(subject):
    return more_or_less_than_average(subject, 1)


def less_than_average(subject):
    return more_or_less_than_average(subject, 0)


def create_table():
    combined = np.column_stack((students, table))
    subjects_list = [""] + subjects
    return tabulate((np.row_stack((subjects_list, combined))), tablefmt="grid")


if __name__ == '__main__':
    print(create_table())
    print(student_with_highest_avg())
    print(highest_score_in_subject('ინგლისური'))
    print(lowest_score_in_subject('მათემატიკა'))
    print(more_than_average("ინგლისური"))
