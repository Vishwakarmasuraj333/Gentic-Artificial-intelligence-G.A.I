# Write a program to implement Delta Rule

def main():
    inputs = []
    weights = []

    n = 3
    lr = float(input("Enter learning rate: "))

    print("Enter input values:")
    for i in range(n):
        x = float(input(f"x{i+1}: "))
        inputs.append(x)

    print("Initialize weight values:")
    for i in range(n):
        w = float(input(f"w{i+1}: "))
        weights.append(w)

    desired_output = float(input("Enter desired output: "))

    for epoch in range(10):
        net_input = 0
        for i in range(n):
            net_input += inputs[i] * weights[i]

        output = net_input
        delta = desired_output - output

        print(f"\nEpoch {epoch+1}")
        print("Net input:", round(net_input, 3))
        print("Delta:", round(delta, 3))

        for i in range(n):
            weights[i] = weights[i] + lr * delta * inputs[i]

        print("Updated weights:", [round(w, 3) for w in weights])

        if abs(delta) < 0.001:
            print("\nOutput is correct")
            break


if __name__ == "__main__":
    main()
