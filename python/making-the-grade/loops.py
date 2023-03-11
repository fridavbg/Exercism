"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = [round(num) for num in student_scores]
    return rounded_scores

# student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
# print(round_scores(student_scores))


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_scores = []
    for score in student_scores:
        if score <= 40:
            failed_scores.append(score)
    return len(failed_scores)

# print(count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]))


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best = []
    for score in student_scores:
        if score >= threshold:
            best.append(score)
    return best

# print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    threshold = int((highest-40)/4)
    letters_grades = []
    for score in range(4):
        letters_grades.append(41 + threshold * score)
    return letters_grades

# print(letter_grades(highest=100))

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    student_rankings = []
    student_scores = zip(student_names, student_scores)
    for idx, ranking in enumerate(student_scores):
        student_rankings.append(str(idx+1) + '. ' + ranking[0] + ': ' + str(ranking[1]))
    return student_rankings

# student_scores = [100, 99, 90, 84, 66, 53, 47]
# student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
# print(student_ranking(student_scores, student_names))

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    res = []
    for info in student_info:
        if info[1] == 100:
            res.append(info)
            return res[0]
    return res

# student_info = [['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]]
# print(perfect_score(student_info))
