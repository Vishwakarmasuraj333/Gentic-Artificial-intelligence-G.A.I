# Write a program for Back Propagation Algorithm
import math

def main():
    coeff = 0.1

    s = [{'val': 0, 'out': 0, 'wo': 0, 'wi': 0, 'top': 0} for _ in range(3)]

    for i in range(3):
        s[i]['val'] = float(input(f"Enter input value for sample {i+1}: "))
        s[i]['top'] = float(input(f"Enter target value for sample {i+1}: "))

    s[0]['wo'] = -1.0
    s[0]['wi'] = -0.3
    s[0]['out'] = 0

    for i in range(1, 3):
        s[i]['wo'] = s[i-1]['wo']
        s[i]['wi'] = s[i-1]['wi']

        s[i]['aop'] = s[i]['wo'] + s[i]['wi'] * s[i]['val']

        s[i]['out'] = 1 / (1 + math.exp(-s[i]['aop']))

        delta = (s[i]['top'] - s[i]['out']) * s[i]['out'] * (1 - s[i]['out'])

        corr = coeff * delta * s[i]['val']

        s[i]['wo'] += corr
        s[i]['wi'] += corr

    print("\nVALUE\tTarget\tActual\two\twi")
    for i in range(3):
        print(f"{s[i]['val']:.3f}\t{s[i]['top']:.3f}\t{s[i]['out']:.3f}\t{s[i]['wo']:.3f}\t{s[i]['wi']:.3f}")


if __name__ == "__main__":
    main()
