import matplotlib.pyplot as plt
import numpy as np

# Data from your dashboard
algorithms = ['STEP-Hide(Custom)', 'LSB', 'LSB+NM', 'F5']

mse = [0.0, 0.5, 0.7, 0.6]                    # Lower is better
psnr = [148.13, 99.26, 99.06, 147.53]          # Higher is better
payload_kb = [710.16, 710.16, 710.16, 710.16]   # Same for all
processing_time = [0.5, 0.8, 1.0, 0.9]          # Lower is better

# Setup for subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Performance Metrics Comparison Across Algorithms', fontsize=16, fontweight='bold')

# Function to add data labels on bars
def add_labels(ax, values):
    for i, v in enumerate(values):
        ax.text(i, v + (max(values) * 0.02), f'{v:.2f}', 
                ha='center', va='bottom', fontsize=8)

# Plot for MSE
axs[0, 0].bar(algorithms, mse, color='lightcoral')
axs[0, 0].set_title('MSE (Lower is Better)', fontsize=11)
axs[0, 0].grid(axis='y', linestyle='--', alpha=0.7)
add_labels(axs[0, 0], mse)

# Plot for PSNR
axs[0, 1].bar(algorithms, psnr, color='deepskyblue')
axs[0, 1].set_title('PSNR (dB) (Higher is Better)', fontsize=11)
axs[0, 1].grid(axis='y', linestyle='--', alpha=0.7)
add_labels(axs[0, 1], psnr)

# Plot for Payload Capacity
axs[1, 0].bar(algorithms, payload_kb, color='mediumseagreen')
axs[1, 0].set_title('Payload Capacity (KB)', fontsize=11)
axs[1, 0].grid(axis='y', linestyle='--', alpha=0.7)
add_labels(axs[1, 0], payload_kb)

# Plot for Processing Time
axs[1, 1].bar(algorithms, processing_time, color='gold')
axs[1, 1].set_title('Processing Time (Lower is Better)', fontsize=11)
axs[1, 1].grid(axis='y', linestyle='--', alpha=0.7)
add_labels(axs[1, 1], processing_time)

# Adjust layout
for ax in axs.flat:
    ax.set_ylabel('Value', fontsize=10)
    #ax.set_xlabel('Algorithm', fontsize=4)
    ax.set_xticklabels(algorithms, rotation=15, fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the figure if you want
# plt.savefig('step_hide_vs_others.png', dpi=300, bbox_inches='tight')

plt.show()
