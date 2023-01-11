import matplotlib.pyplot as plt
import numpy as np

pos_x_arr = []
pos_y_arr = []

file = open('camera_pos.csv', 'r+')

for line in file.readlines():
    xy = line.strip('\n').split(',')
    pos_x_arr.append(float(xy[0]))
    pos_y_arr.append(float(xy[1]))

pos_x_lp = [0]*3
for i in range(4, len(pos_x_arr)):
    pos_x_lp.append(sum(pos_x_arr[i-4:i])/5)

plt.plot(pos_x_arr[:], 'b', label='pos x')
plt.plot([pos_x_arr[i] - pos_x_arr[i-1] for i in range(1, len(pos_x_arr))], 'r', label='derivada')

pos_FFT = np.fft.fft(pos_x_arr)

plt.minorticks_on()
#plt.semilogy(np.fft.fftshift(np.fft.fftfreq(len(pos_FFT))),np.abs(np.fft.fftshift(pos_FFT)))

#plt.plot(pos_x_lp[:], 'k', label='pos x lp')
#plt.plot([pos_x_lp[i] - pos_x_lp[i-1] for i in range(1, len(pos_x_lp))], 'k', label='derivada lp')

#plt.plot(integral[1:], 'k', label='integral')

#plt.plot([p*100 for p in pos_y_arr[:]], 'r')
plt.legend()
plt.show()