# Write a program to implement Hebb’s Rule.

def main():
    w = float(input("Consider a single neuron perceptron with a single i/p (initial weight): "))
    d = float(input("Enter the learning coefficient: "))
    x = float(input("Enter the input value: "))
    t = float(input("Enter the target output: "))

    for i in range(10):
        net = x * w
        a = 1 if net >= 0 else 0
        dw = d * x * t
        w = w + dw

        print("Iteration:", i + 1,
              "Output:", a,
              "Change in weight:", round(dw, 3),
              "Adjusted weight:", round(w, 3))


if __name__ == "__main__":
    main()
