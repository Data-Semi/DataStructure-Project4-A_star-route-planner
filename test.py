from helpers import load_map
from student_code import shortest_path

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]

MAP_10_ANSWERS = [
    (4, 9, -1)
]

def test(shortest_path_function):
    map_40 = load_map('map-40.pickle')
    map_10 = load_map('map-10.pickle')
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start, 
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases in map 40")

#add map 10 test case: the goal is unreachable
    for start, goal, answer_path in MAP_10_ANSWERS:
        path = shortest_path_function(map_10, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start, 
                "Goal:     ", goal,
                "Your path:", path,
                "Correct:  ", answer_path)
    if correct == len(MAP_10_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_10_ANSWERS), "test cases in map 10")

# if __name__ == "__main__":
#     test(shortest_path)