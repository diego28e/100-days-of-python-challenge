student_scores=[78,65,89,86,55,91,64,89,95]
length=len(student_scores)

total_exam_score = sum(student_scores)
average_score = round((total_exam_score/length),2)
print(total_exam_score)
print(average_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)
print(round(sum/length, 2))