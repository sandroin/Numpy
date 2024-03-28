# Numpy
This Python script is for generating random student names and associated scores in various subjects using numpy. 

# Data setup
1. subjects: A list containing the names of different subjects.
2. first_names and last_names: Lists of Georgian first names and last names respectively, used for generating random student names.
3. students: A list comprehension that generates random student names.
4. table: A NumPy array of random integer scores for each student and subject.

# Functions:
1. generate_random_name(): Generates a random full name for a student.
2. student_with_highest_avg(): Finds the student(s) with the highest average score across all subjects.
3. calculate_index(): Helper function to get the index of a subject in the subjects list.
4. extremum_score_in_subject(): Finds the student(s) with the highest or lowest score in a given subject.
5. highest_score_in_subject() and lowest_score_in_subject(): Wrapper functions for finding the highest and lowest scores in a subject.
6. more_or_less_than_average(): Finds students with scores higher or lower than the average in a given subject.
7. more_than_average() and less_than_average(): Wrapper functions for finding students with scores higher or lower than the average in a subject.
8. create_table(): Generates a tabulated representation of student scores.
