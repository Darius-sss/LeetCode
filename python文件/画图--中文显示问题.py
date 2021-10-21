import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = range(-20, 20)
y = list(map(lambda x:x**2, x))
print(y)
plt.title('林之博')
plt.plot(x, y)
plt.show()