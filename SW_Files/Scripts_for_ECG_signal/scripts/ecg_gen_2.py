import numpy as np

data = np.loadtxt('ecg_signal.txt')
t_orig = data[:, 0]
v_orig = data[:, 1]

mask = t_orig <= 5.0
t_5s = t_orig[mask]
v_5s = v_orig[mask]

t_new = np.linspace(0, 5.0, 150)
v_new = np.interp(t_new, t_5s, v_5s)

with open("ecg_signal_5per_2.txt", "w") as f:
    f.write("{PRIMITIVE=ANALOGUE\n")
    f.write("DC=0V\n")
    
    for i in range(len(t_new)):
        f.write(f"T{i}={t_new[i]:.4f}\n")
        f.write(f"V{i}={v_new[i]:.6f}V\n")
        
    f.write("\n}")
