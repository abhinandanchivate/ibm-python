##You want to store scores for students in various subjects, where the subjects are nested within each student's name. {
#     'Alice': {
#         'Math': [85, 90],
#         'Science': [78, 88]
#     },
#     'Bob': {
#         'Math': [92],
#         'History': [81, 73]
#     }
# }

# scores = {}
# scores['Alice'] = {'Math': [85, 90], 'Science': [78, 88]}
# scores['Bob'] = {'Math': [92], 'History': [81, 73]}
# # scores['Alice']['Math'] = [85, 90]
# # scores['Alice']['Science'] = [78, 88]
# using defaultDict
from collections import defaultdict
from pprint import pprint

# Create a defaultdict with a nested structure
scores = defaultdict(lambda: defaultdict(list))
# Add scores for Alice
scores['Alice']['Math'].append(85)
scores['Alice']['Math'].append(90)
scores['Alice']['Science'].append(78)
scores['Alice']['Science'].append(88)
# Add scores for Bob
scores['Bob']['Math'].append(92)
scores['Bob']['History'].append(81)
scores['Bob']['History'].append(73)
# Print the scores
# for student, subjects in scores.items():
#     print(f"{student}:")
#     for subject, scores_list in subjects.items():
#         print(f"  {subject}: {scores_list}")
print(dict(scores))