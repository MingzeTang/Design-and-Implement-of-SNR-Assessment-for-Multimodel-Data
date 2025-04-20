import numpy as np
import torch
import librosa


def sisnr(x, s, eps=1e-8):
    def l2norm(mat, keepdim=False):
        return torch.norm(mat, dim=-1, keepdim=keepdim)

    if x.shape != s.shape:
        raise RuntimeError("Dimension mismatch when calculating SI-SNR, {} vs {}".format(x.shape, s.shape))

    x_zm = x - torch.mean(x, dim=-1, keepdim=True)  # Zero-mean of the separated signal
    s_zm = s - torch.mean(s, dim=-1, keepdim=True)  # Zero-mean of the reference signal
    t = torch.sum(x_zm * s_zm, dim=-1, keepdim=True) * s_zm / (l2norm(s_zm, keepdim=True) ** 2 + eps)

    return -40 * torch.log10(eps + l2norm(t) / (l2norm(x_zm - t) + eps))


# SI-SNR to SNR conversion
def si_snr_to_snr(si_snr_db, alpha):
    si_snr_lin = 10 ** (si_snr_db / 10)
    snr_lin = 1 / ((alpha - 1) ** 2 + (alpha ** 2) / si_snr_lin)
    return 10 * np.log10(snr_lin)


# Load WAV files
def load_wav(filename):
    signal, sr = librosa.load(filename, sr=None)  # sr=None to keep original sampling rate
    return signal, sr


# Convert WAV signal to tensor
def wav_to_tensor(signal):
    return torch.tensor(signal).unsqueeze(0)  # Convert to 2D tensor (1, S)


# Example: Load the noisy and denoised WAV files
x_signal, sr = load_wav('original_path')  # Noisy signal
s_signal, sr = load_wav('denoised_path')  # Clean signal as the reference signal

# Ensure both signals have the same length (truncate or pad with zeros)
min_length = min(len(x_signal), len(s_signal))
x_signal = x_signal[:min_length]
s_signal = s_signal[:min_length]

# Convert to tensors
x_tensor = wav_to_tensor(x_signal)
s_tensor = wav_to_tensor(s_signal)

# Calculate SI-SNR
si_snr_value = sisnr(x_tensor, s_tensor).item()

# Estimate alpha (assuming it's provided or pre-calculated)
alpha = 0.9

# Convert SI-SNR to SNR
snr_pred = si_snr_to_snr(si_snr_value, alpha)

# Output the results
print(f"SNR: {snr_pred:.2f} dB")
