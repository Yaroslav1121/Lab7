import matplotlib.pyplot as plt

with open("words.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')
    rozp = 0
    oklychni = 0
    pytalni = 0
    trikrapki = 0
    for char in data:
        if char == "!":
            oklychni = oklychni + 1
        elif char == "...":
            trikrapki = trikrapki + 1
        elif char == ".":
            rozp = rozp + 1
        elif char == "?":
            pytalni = pytalni + 1
sentences = [rozp, pytalni, oklychni, trikrapki]
print(sentences)
x = sentences
y = ("Розповідні", "Питальні", "Окличні", "Три крапки")

fig, ax = plt.subplots()

width = 0.6
ax.bar(y, x, width=width, color='orange')

fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')
ax.set_facecolor('oldlace')
plt.show()
fig.savefig('saved_figure.png', dpi=300)

