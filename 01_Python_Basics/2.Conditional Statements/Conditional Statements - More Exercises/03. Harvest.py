import math
area = int(input())
grape_meter = float(input())
need_vine = int(input())
workers = int(input())
area_for_vine = area * 0.4
kg_grape = grape_meter * area_for_vine
vine = kg_grape / 2.5
vine_remaining = abs(vine - need_vine)
vine_for_workers = vine_remaining / workers
if vine < need_vine:
    print(f"It will be a tough winter! More {math.floor(vine_remaining)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(vine)} liters.")
    print(f"{math.ceil(vine_remaining)} liters left -> {math.ceil(vine_for_workers)} liters per person.")