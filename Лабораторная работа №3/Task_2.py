def find_common_participants(group1, group2, a=','):
    list1 = group1.split(a)
    list2 = group2.split(a)
    common = list(set(list1).intersection(list2))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники:", find_common_participants(participants_first_group, participants_second_group))
