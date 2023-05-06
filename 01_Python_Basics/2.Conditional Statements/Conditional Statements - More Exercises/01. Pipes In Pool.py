V = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
p1_h = h * p1
p2_h = h * p2
total = p1_h + p2_h
total_percent = (total * 100) / V
remaining = total - V
p1_percent = (p1_h * 100) / total
p2_percent = (p2_h * 100) / total

if total <= V:
    print(f"The pool is {total_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {remaining:.2f} liters.")