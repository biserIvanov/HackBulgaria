import requests
import random


class Simple(object):

    def __init__(self, courses_list, courses_dct, allThe):
        self.courses_list = courses_list
        self.courses_dct = courses_dct
        self.allThe = allThe

    def courses_iteration(self, info):
        for dct in info:
            for list_element in dct["courses"]:
                if not list_element["name"] in self.courses_list:
                    self.courses_list.append(list_element["name"])
        a = 1
        for course in self.courses_list:
            self.courses_dct[a] = course
            a += 1

    def match_people(self, course_id, team_size, group_time):
        # лист със всички хора които са с course_id и group_time - еднакви
        current_list = []
        current_dct = {}
        current_dct["group"] = group_time
        current_dct["name"] = self.courses_dct[course_id]
        print(current_dct)
        for dct in self.allThe:
            for dct_element in dct["courses"]:
                if dct_element == current_dct:
                    current_list.append(dct['name'])

        while len(current_list) > 3:
            current_team = []
            for i in range(team_size):
                choice = random.randint(0, len(current_list)-1)
                current_team.append(current_list[choice])
                current_list.remove(current_list[choice])
            print(current_team)
        print(current_list)


def main():
    obj = Simple([], {}, [])
    a = "0"
    while a != "exit":
        a = input("Hello, you can use one the the following commands:\n\
            - list_courses - this lists all the courses that are available now.\n\
            - match_teams <course_id>, <team_size>, <group_time>\n\
            - exit\n")
        if a == "list_courses":
            print("list_courses:")
            allTheRubish = requests.get('https://hackbulgaria.com/api/students/', verify=False)
            obj.allThe = allTheRubish.json()
            obj.courses_iteration(obj.allThe)
            for a in range(1, len(obj.courses_dct)):
                print("[" + str(a) + "]" + obj.courses_dct[a])
        elif "match_teams" in a:
            arguments = []
            a = a[12:]
            arguments = a.split()
            obj.match_people(int(arguments[0]), int(arguments[1]), int(arguments[2]))
        elif a == "exit":
            pass
        else:
            print("ivalid input")

if __name__ == '__main__':
    main()
