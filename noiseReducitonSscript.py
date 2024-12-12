import numpy as np
from scipy.signal import butter, filtfilt, find_peaks, windows
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Function to apply a bandpass filter
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

# Take input file path and output file path from the user
input_file = input("Enter the path of the input audio file (e.g., C:\\path\\to\\file.wav): ")
output_file = input("Enter the path where you want to save the filtered audio file (e.g., C:\\path\\to\\output.wav): ")

# Load the audio file
sample_rate, audio = wavfile.read(input_file)

# Convert stereo to mono if necessary
if len(audio.shape) > 1:
    audio = audio.mean(axis=1)

audio = audio.astype(np.float64)

# Apply windowing to smooth the spectrum
window = windows.hamming(len(audio))
windowed_audio = audio * window

# Apply bandpass filter (adjust lowcut and highcut for your needs)
lowcut = 50  # Lower bound frequency in Hz
highcut = 5000  # Upper bound frequency in Hz
filtered_audio = bandpass_filter(windowed_audio, lowcut, highcut, sample_rate)

# Perform FFT
fft_spectrum = np.fft.fft(filtered_audio)
frequencies = np.fft.fftfreq(len(filtered_audio), d=1/sample_rate)
magnitude = np.abs(fft_spectrum)

# Detect peaks in the spectrum
peaks, _ = find_peaks(magnitude, height=1e5, distance=20)  # Adjust parameters as needed

# Plot the original and filtered spectrum
plt.figure(figsize=(10, 6))

# Original Spectrum
plt.subplot(2, 1, 1)
original_fft_spectrum = np.fft.fft(audio)
original_magnitude = np.abs(original_fft_spectrum)
plt.plot(frequencies[:len(frequencies)//2], original_magnitude[:len(frequencies)//2])
plt.title("Original Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

# Filtered Spectrum
plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], magnitude[:len(frequencies)//2], label="Filtered Spectrum")
plt.scatter(frequencies[peaks], magnitude[peaks], color='orange', label="Peaks")
plt.title("Filtered Frequency Spectrum with Peaks")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()

# Save the filtered audio back to a file
wavfile.write(output_file, sample_rate, filtered_audio.astype(np.int16))
