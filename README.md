
# Audio Noise Reduction

This project implements an audio noise reduction algorithm to clean up noisy audio recordings. The algorithm uses filtering techniques, Fourier Transform, and time-frequency analysis to attenuate unwanted noise.

## Features
- Analyze noisy audio files to identify dominant frequencies.
- Apply a bandpass filter to attenuate unwanted noise frequencies.
- Visualize the frequency spectrum before and after noise reduction.
- Save the filtered audio for further use.

## Prerequisites

### Python Installation
Ensure that you have Python 3.7 or higher installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### Dependencies
The following Python libraries are required:
- `numpy`
- `scipy`
- `matplotlib`

To install these dependencies, open a terminal (or command prompt) and run:
```bash
pip install numpy scipy matplotlib
```

## How to Use

1. **Clone or Download the Project**
   Download this project and navigate to its folder.

2. **Prepare an Audio File**
   Ensure that you have a `.wav` audio file to process. Place it in an easily accessible location.

3. **Run the Script**
   Open a terminal or command prompt in the project folder and run:
   ```bash
   python audio_noise_reduction.py
   ```

4. **Provide File Paths**
   When prompted:
   - Enter the path of the input audio file (e.g., `C:\path\to\input.wav`).
   - Enter the path to save the output filtered audio file (e.g., `C:\path\to\output.wav`).

5. **View the Spectrum Analysis**
   The script will display plots showing the original and filtered frequency spectrums, along with detected peaks.

6. **Check the Output File**
   The filtered audio will be saved at the location specified in the second step.

## How It Works

### Key Concepts
- **Filtering:** A bandpass filter is used to attenuate frequencies outside the specified range.
- **Fourier Transform:** Used to analyze the frequency content of the audio signal.
- **Peak Detection:** Identifies dominant frequencies in the spectrum.

### Workflow
1. The script reads the audio file and converts it to mono if necessary.
2. A Hamming window is applied to smooth the spectrum.
3. A bandpass filter attenuates frequencies outside the specified range (default: 50 Hz to 5000 Hz).
4. The script computes the FFT and identifies peaks in the filtered spectrum.
5. Plots are displayed for visual comparison of the original and filtered spectra.
6. The filtered audio is saved to the specified file path.

## Notes
- Adjust the `lowcut` and `highcut` variables in the script to change the bandpass filter range.
- You can tweak the peak detection parameters (e.g., `height` and `distance`) for different results.

## Authors 
- Islam Mohamad Gomaa
- Mokhtar wael 
- Anas osama

