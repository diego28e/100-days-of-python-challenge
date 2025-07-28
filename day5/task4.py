student_scores=[78,65,89,86,55,91,64,89,95,25]

max_number=max(student_scores)
print(max_number)

max_score=0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)