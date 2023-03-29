class Vector:
    """
    Класс описывает векторы и их поведение.
    cosX, cosY, cosZ - направляющие косинусы вектора.
    name - название вектора.
    begin и end - координаты начала и конца вектора соответственно.
    coords - координаты вектора.
    length - длина вектора.
    """
    def __init__(self, end, begin = (0, 0, 0), name = "vector"):
        """
            Количество элементов в кортеже end должно совпадать с таковым в begin.
            :param end: Передаётся кортеж, состоящий из 2 или 3 координат.
            :param begin: Передаётся кортеж, состоящий из 2 или 3 координат.
            :param name: Передаётся имя вектора, если таковое имеется.
        """
        if len(begin) > 3 and len(end) > 3 and len(end) > len(begin):
            raise Exception("Количество указанных координат не соответствует требованиям.")
        var = 0
        coords = []
        for i in range(len(end)):
            coords.append(end[i] - begin[i])
            var += (end[i] - begin[i]) ** 2
        self.length = var ** (1/2)
        self.begin = begin
        self.end = end
        if len(coords) == 2:
            coords.append(0)
        self.coords = tuple(coords)
        self.name = name
        self.cosX = coords[0] / self.length
        self.cosY = coords[1] / self.length
        self.cosZ = coords[2] / self.length

    def setName(self, name):
        self.name = name

    def __add__(self, v2):
        return Vector((self.coords[0] + v2.coords[0], self.coords[1] + v2.coords[1], self.coords[2] +\
                       v2.coords[2]), self.begin)

    def __sub__(self, v2):
        return Vector((self.coords[0] - v2.coords[0], self.coords[1] - v2.coords[1], self.coords[2] - \
                       v2.coords[2]), self.begin)

    def __mul__(self, num):
        return Vector((self.coords[0] * num, self.coords[1] * num, self.coords[2] * num), self.begin)

    def __str__(self):
        return "Вектор " + str(self.name) + ".\nКоординаты:\nx: " +\
        str(self.coords[0]) + ";\ny: " + str(self.coords[1]) + ";\nz: " + \
        str(self.coords[2]) + ".\nДлина вектора: " + str(self.length) + "."


def scal_prod(vector1, vector2):
    """
    Функция находит скалярное произведение векторов, указанных в аргументах.
    :param vector1: Вектор 1.
    :param vector2: Вектор 2.
    :return: Возвращает скалярное произведение векторов.
    """
    count = min(len(vector1.coords), len(vector2.coords))
    result = 0
    for i in range(count):
        result += vector1.coords[i] * vector2.coords[i]
    return result


def are_complanar(vector1, vector2, vector3):
    """
    Возвращает булево значение. Определяет, компланарны ли векторы или нет.
    :param vector1: Вектор-1.
    :param vector2: Вектор-2.
    :param vector3: Вектор-3.
    :return: True, если компланарные векторы и False, если нет.
    """
    if mixed_prod(vector1, vector2, vector3):
        return False
    else:
        return True


def v_prod(vector1, vector2):
    """
    Возвращает векторное произведение 2 векторов.
    :param vector1: Вектор-1.
    :param vector2: Вектор-2.
    :return: Возвращает вектор, являющийся векторным произведением 2 других векторов.
    """
    x = vector1.coords[1] * vector2.coords[2] - vector1.coords[2] * vector2.coords[1]
    y = -vector1.coords[0] * vector2.coords[2] + vector1.coords[2] * vector2.coords[0]
    z = vector1.coords[0] * vector2.coords[1] - vector1.coords[1] * vector2.coords[0]
    return Vector((x, y, z))


def v_move(vector, coords_of_begin):
    """
    Перемещает начало вектора в пространстве.
    :param vector: Вектор.
    :param coords_of_begin: Кортеж. Новые координаты начала.
    :return: Вектор с новыми координатами начала.
    """
    if len(coords_of_begin) > 3:
        raise Exception("Передано слишком много координат.")
    lst_c = list(coords_of_begin)
    while len(lst_c) < 3:
        lst_c.append(0)
    vector.begin = tuple(lst_c)
    vector.end = tuple([lst_c[0] + vector.coords[0], lst_c[1] + vector.coords[1], lst_c[2] + vector.coords[2]])


def cos_ang_vecs(vector1, vector2):
    """
    Возвращает косинус угла между указанными в аргументах векторами.
    :param vector1: Вектор-1.
    :param vector2: Вектор-2.
    :return: Косинус угла между указанными векторами.
    """
    return scal_prod(vector1, vector2) / (vector1.length * vector2.length)


def mixed_prod(vector1, vector2, vector3):
    """
    Возвращает смешанное произведение векторов.
    :param vector1: Вектор-1.
    :param vector2: Вектор-2.
    :param vector3: Вектор-3.
    :return: Смешанное произведение векторов.
    """
    result = vector1.coords[0] * vector2.coords[1] * vector3.coords[2] + vector1.coords[1] \
             * vector2.coords[2] * vector3.coords[0] + \
             vector2.coords[0] * vector3.coords[1] * vector1.coords[2] - \
             vector1.coords[2] * vector2.coords[1] * vector3.coords[0] - \
             vector1.coords[1] * vector2.coords[0] * vector3.coords[2] \
             - vector2.coords[2] * vector3.coords[1] * vector1.coords[0]
    return result


def vector_proj(vector1, vector2):
    """
    Возвращает длину проекции вектора-1 на вектор-2.
    :param vector1: Вектор-1.
    :param vector2: Вектор-2.
    :return: Скалярная величина проекции вектора-1 на вектор-2.
    """
    return scal_prod((vector1, vector2) / vector2.length)


def are_collinear(vector1, vector2):
    """
    Определяет коллинеарность векторов.
    :param vector1: Вектор-1.
    :param vector2: Вектор-2.
    :return: True, если коллинеарны, и False, если нет.
    """
    if v_prod(vector1, vector2):
        return False
    else:
        return True

def are_perpendicular(vector1, vector2):
    """
    Определяет перпендикулярность векторов.
    :param vector1: Вектор-1.
    :param vector2: Вектор-2.
    :return: True, если перпендикулярны, и False, если нет.
    """
    if scal_prod(vector1, vector2):
        return False
    else:
        return True

