import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
fs = 250                   # Sampling frequency (Hz)
duration = 300             # Signal duration (seconds)
heart_rate = 60            # Heart rate (beats per minute)
samples = fs * duration

# Time vector
t = np.linspace(0, duration, samples)

# Gaussian wave function
def gaussian(t, mu, sigma, amplitude):
    return amplitude * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

# Cardiac period (seconds per beat)
T = 60 / heart_rate

# Initialize ECG signal
ecg = np.zeros_like(t)

# Generate ECG waveform (P-Q-R-S-T model)
for beat in np.arange(0, duration, T):
    ecg += gaussian(t, beat + 0.1,  0.025,  0.15)   # P wave
    ecg += gaussian(t, beat + 0.2,  0.010, -0.10)   # Q wave
    ecg += gaussian(t, beat + 0.22, 0.008,  1.00)   # R wave
    ecg += gaussian(t, beat + 0.25, 0.010, -0.25)   # S wave
    ecg += gaussian(t, beat + 0.35, 0.040,  0.30)   # T wave

# Normalize to +-1mV (+-0.001 V)
ecg = (ecg / np.max(np.abs(ecg))) * 0.001

# Save signal to text file (Proteus File Signal Generator compatible)
with open("ecg_signal.txt", "w") as f:
    for ti, vi in zip(t, ecg):
        f.write(f"{ti:.6f} {vi:.6f}\n")

print("ecg_signal.txt file generated successfully!")

# plt.figure()
# plt.plot(t, ecg)
# plt.xlabel("Time [s]")
# plt.ylabel("Amplitude [V]")
# plt.title("Synthetic ECG Signal")
# plt.grid(True)
# plt.show()
