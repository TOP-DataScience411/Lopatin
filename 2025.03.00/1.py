import resurses
from pathlib import Path
from Task_solver import task_solver


if (Path.cwd()/"data.pic").exists():
    data = resurses.load_pic_instance()
else:
    data = resurses.fixproblem(resurses.get_data(resurses.find_Morozoff()))
while True:
    variant = input("введите номер варианта: ")
    if variant.isdigit() and 0<int(variant) <= 20:
        break

variant = data[int(variant)-1]
level_of_significance = 0.05
N = variant["N"]
R = variant['R']

analyser =  task_solver(N,R)
results = analyser.analyze()
analyser.print_results()