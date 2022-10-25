import numpy as np
import matplotlib.pyplot as plt


v_x = []
v_y = []
v = []

for k in range(1,50):
    filnavn = f'mass8_{k}.txt'
    data = open(filnavn)

#print(open(filnavn).read(), '  ')

    t = []
    x = []
    y = []
    i = 0
    for line in open(filnavn):
        i += 1
        z = 0
        for number in line.split():
            z += 1
            if i > 2 and z == 1:
                t.append(float(number))
            elif i > 2 and z == 2:
                x.append(float(number))
            elif i > 2 and z == 3:
                y.append(float(number))

    t = np.array(t)
    x = np.array(x)
    y = np.array(y)


    for i in range(0,len(t)-1):
        v_x.append((x[i+1]-x[i])/(t[i+1]-t[i]))
        v_y.append((y[i + 1] - y[i]) / (t[i + 1] - t[i]))
        v.append(np.sqrt(((x[i+1]-x[i])/(t[i+1]-t[i]))**2+((y[i + 1] - y[i]) / (t[i + 1] - t[i]))**2))

    plt.figure(5)
    plt.scatter(x, y, c="b", marker="o", alpha=0.3)
    plt.xlabel("x(cm)")
    plt.ylabel("y(cm)")
    plt.grid()

v = np.array(v)
v_x = np.array(v_x)
v_y = np.array(v_y)

B = 1/np.mean(v**2)









plt.figure(6)
plt.scatter(v_x,v_y,c="b",marker="x",label=f"〈v_x〉= {np.mean(v_x):.2f},〈v_y〉= {np.mean(v_y):.2f}")
plt.scatter(np.mean(v_x),np.mean(v_y), marker="*", c="r", label=f"〈v_x〉= {np.mean(v_x):.2f},〈v_y〉= {np.mean(v_y):.2f}")
plt.xlabel("v_x(cm/s)")
plt.ylabel("v_y(cm/s)")
plt.grid()
plt.legend()

f_v = 2*B*v*np.e**(-B*v**2)
g_vx = np.sqrt(B/np.pi)*np.e**(-B*v_x**2)
g_vy = np.sqrt(B/np.pi)*np.e**(-B*v_y**2)

f = np.linspace(int(np.min(v)),int(np.max(v)),21)
g_x = np.linspace(int(np.min(v_x)),int(np.max(v_x)),21)
g_y = np.linspace(int(np.min(v_y)),int(np.max(v_y)),21)
antall = np.arange(0,len(v),1)

plt.figure(1)
plt.plot(antall, v)

plt.figure(2)
plt.hist(v,bins=20, density=True, facecolor='g', alpha=0.75)
plt.plot(f , 2*B*f*np.e**(-B*f**2),marker="o", ls="none")
plt.grid()

plt.figure(3)
plt.hist(v_x,bins=20, density=True, facecolor='g', alpha=0.75)
plt.plot(g_x , np.sqrt(B/np.pi)*np.e**(-B*g_x**2),marker="o", ls="none")

plt.figure(4)
plt.hist(v_y,bins=20, density=True, facecolor='g', alpha=0.75)
plt.plot(g_y, np.sqrt(B/np.pi)*np.e**(-B*g_y**2),marker="o", ls="none")

plt.show()

m = 32*10**(-3)
T = 300

k_p = (0.5*m*np.mean(v**2))/T

print(f"Boltzmanns plastskive konstant blir {k_p:.2f}")

midlere_v = np.mean(v)
v_rms = np.sqrt(np.mean(v**2))

if np.pi-0.1 < midlere_v/v_rms < np.pi/2+0.1:
    print(f"Forholdet mellom midlere v og v_rms er π/2")
else:
    print(f"Forholdet mellom midlere v og v_rms er {midlere_v/v_rms:.2f}, π/2 = {np.pi/2:.2f}")

