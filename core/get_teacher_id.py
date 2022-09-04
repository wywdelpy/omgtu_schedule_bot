def get_teacher_id(name):
    if '.' in name:
        name = name.replace('.',' ')
        name = name.split()
    all_teachers = []


    with open ('all_teachers_id.txt','r') as file:
        all_teachers = file.readlines()
        for teacher in all_teachers:
            teacher = teacher.replace('\n','')
            teacher_ziped = teacher.split(' : ')
            teacher_ziped = teacher_ziped[0].split()
            if type(name) is list:
                if name[0].upper() == teacher_ziped[0].upper():
                    if name[1].upper() in teacher_ziped[1].upper():
                        if name[2].upper() in teacher_ziped[2].upper():
                            teacher = teacher.split(' : ')
                            id = teacher[1]
                            # print(id)
                            return id
            else:
                if name.upper() == teacher_ziped[0].upper():
                    teacher = teacher.split(' : ')
                    id = teacher[1]
                    # print(id)
                    return id
        return f'<b>Преподатель с такой фамилией не найден!</b>\nПопробуйте еще раз'

# get_teacher_id('панин')
