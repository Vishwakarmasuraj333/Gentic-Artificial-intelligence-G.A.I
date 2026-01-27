#Write a program for Hopfield Network.
class Neuron:
    def __init__(self, weights):
        self.weightv = weights
        self.activation = 0

    def act(self, m, x):
        a = 0
        for i in range(m):
            a += x[i] * self.weightv[i]
        return a


class Network:
    def __init__(self, a, b, c, d):
        self.nrn = [Neuron(a), Neuron(b), Neuron(c), Neuron(d)]
        self.output = [0] * 4

    def threshld(self, k):
        return 1 if k >= 0 else 0

    def activation(self, patrn):
        for i in range(4):
            for j in range(4):
                print(f"nrn[{i}].weightv[{j}] is {self.nrn[i].weightv[j]}")
            self.nrn[i].activation = self.nrn[i].act(4, patrn)
            print(f"activation is {self.nrn[i].activation}")
            self.output[i] = self.threshld(self.nrn[i].activation)
            print(f"output value is {self.output[i]}\n")


def main():
    patrn1 = [1, 0, 1, 0]
    patrn2 = [0, 1, 0, 1]

    wt1 = [0, -3, 3, -3]
    wt2 = [-3, 0, -3, 3]
    wt3 = [3, -3, 0, -3]
    wt4 = [-3, 3, -3, 0]

    print("\nTHIS PROGRAM IS FOR A HOPFIELD NETWORK WITH 4 FULLY INTERCONNECTED NEURONS")
    print("THE NETWORK SHOULD RECALL THE PATTERNS 1010 AND 0101 CORRECTLY.\n")

    h1 = Network(wt1, wt2, wt3, wt4)

    print("Presenting pattern 1010:")
    h1.activation(patrn1)
    for i in range(4):
        if h1.output[i] == patrn1[i]:
            print(f"pattern= {patrn1[i]}  output= {h1.output[i]}  component matches")
        else:
            print(f"pattern= {patrn1[i]}  output= {h1.output[i]}  discrepancy occurred")

    print("\nPresenting pattern 0101:")
    h1.activation(patrn2)
    for i in range(4):
        if h1.output[i] == patrn2[i]:
            print(f"pattern= {patrn2[i]}  output= {h1.output[i]}  component matches")
        else:
            print(f"pattern= {patrn2[i]}  output= {h1.output[i]}  discrepancy occurred")


if __name__ == "__main__":
    main()
