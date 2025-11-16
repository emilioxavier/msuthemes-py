"""Basic usage example for MSUthemes.

This script demonstrates the simplest way to create MSU-branded visualizations.
"""

import matplotlib.pyplot as plt
import numpy as np
from msuthemes import theme_msu, colors

# Apply MSU theme
theme_msu()

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot with MSU Green
ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2, label='sin(x)')

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Basic MSU-Branded Plot')
ax.legend()

# Save and show
plt.tight_layout()
plt.savefig('examples/output/basic_usage.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/basic_usage.png")
plt.show()
