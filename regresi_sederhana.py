import numpy as np
import pandas as pd

data = pd.read_csv('pekerja.csv')
x = data['bb']
y = data['tinggibb']
print("M Harits Rasyid R (15-2017-118)")
print()

print("Data tinggi dan berat badan pekerja")
print()
print(data.head())
print()


def linear_regression(x, y):
    N = len(x)
    x1 = x.sum()
    y1 = y.sum()
    x2 = round((x ** 2).sum(), 3)
    y2 = round((y ** 2).sum(), 3)
    xy = round((x * y).sum(), 3)
    print("Jumlah data = ", N)
    print("Σx =", x1)
    print("Σy =", y1)
    print("x2 =", x2)
    print("y2 =", y2)
    print("Σxy =", xy)
    print()

    # (∑Yi)(∑Xi^2)
    a1 = round((y1 * x2), 3)
    print("(∑Yi)(∑Xi^2) = ", a1)

    # (∑Xi)(∑XiYi)
    a2 = round((x1 * xy), 3)
    print("(∑Xi)(∑XiYi) = ", a2)

    # nΣXi^2
    a3 = round((N * x2), 3)
    print(" nΣXi^2      = ", a3)

    # (ΣXi)^2
    a4 = round((x1 ** 2), 3)
    print("(ΣXi)^2      = ", a4)

    # (∑Yi)(∑X^2 i) - (∑Xi)(∑XiYi)
    a5 = round((a1 - a2), 3)
    print("(∑Yi)(∑X^2 i) - (∑Xi)(∑XiYi) = ", a5)

    # nΣXi^2 -  (ΣXi)^2
    a6 = round((a3 - a4), 3)
    print("nΣXi^2 - (ΣXi)^2 = ", a6)

    a = round((a5 / a6), 3)
    print("a = ", a)
    print()

    # nΣXiYi
    b1 = round((N * xy), 3)
    print("nΣXiYi     = ", b1)

    # (Σxi)(Σyi)
    b2 = round((x1 * y1), 3)
    print("(Σxi)(Σyi) = ", b2)

    # nΣXi
    b3 = round((N * x1), 3)
    print("nΣXi       = ", b3)

    # (Σxi)^2
    b4 = round((x1 ** 2), 3)
    print("(Σxi)^2    = ", b4)

    # nΣXiYi - (Σxi)(Σyi)
    b5 = round((b1 - b2), 3)
    print("nΣXiYi - (Σxi)(Σyi) = ", b5)

    # nΣXi - (Σxi)^2
    b6 = round((b3 - b4), 3)
    print("nΣXi - (Σxi)^2 = ", b6)

    b = round((b5 / b6), 3)
    print("b = ", b)

    reg_line = 'y = {} + {}x'.format(a, b)
    return (a, b, reg_line)


def corr_coef(x, y):
    N = len(x)
    num = (N * (x * y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x ** 2).sum() - x.sum() ** 2) * (N * (y ** 2).sum() - y.sum() ** 2))
    R = num / den
    return R

def predict(a, b, new_x):
    y = a + b * new_x
    return y

a, b, reg_line = linear_regression(x, y)
p = ""
print()
print('Persamaan Regresi Linear: ', reg_line)
R = round(corr_coef(x, y), 3)
print('Nilai Korelasi Pearson: ', R)
if R < 0.2:
    print('Skala Guilford = Sangat Lemah')
elif R <= 0.4:
    print('Skala Guilford = Lemah')
elif R <= 0.6:
    print('Skala Guilford = Sedang')
elif R <= 0.8:
    print('Skala Guilford = Kuat')
elif R <= 1:
    print('Skala Guilford = Sangat Kuat')
else:
    print("-")

print('Koefesien determinasi: ', round(R ** 2, 3) * 100, '%')
print()
print('')
i = float(input("Masukan nilai X : "))
print("x = ", i)
print("y =", a, " + ", b, "x")
print("y =", a, " + ", b, "(", i, ")")
print("y = ", round(predict(a, b, i), 3))