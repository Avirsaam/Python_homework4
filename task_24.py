# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

crop_by_bush = [10, 2, 3, 4, 1, 11]

best_crop  = 0
index_of_best_position = 0

for this_bush in range(len(crop_by_bush)):
    if this_bush - 1 < 0:
        previous_bush = crop_by_bush[-1]
    else:
        previous_bush = this_bush - 1

    if this_bush + 1 > len(crop_by_bush):
        next_bush = crop_by_bush[1]
    else:
        next_bush = this_bush + 1

    this_bushes = [previous_bush, crop_by_bush[this_bush], next_bush]
    crop_in_this_position = 0

    for bush in this_bushes:
        crop_in_this_position += bush

    if crop_in_this_position > best_crop:
        index_of_best_position = this_bush
        best_crop = crop_in_this_position

print('Максимальное число ягод', best_crop, 'за один раз, можно собрать в с куста', index_of_best_position + 1)
