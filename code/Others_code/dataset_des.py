import os
import matplotlib.pyplot as plt
import numpy as np

# Path to the main dataset directory
dataset_path = 'collected_data'

# Initialize a dictionary to hold the count of images per class
class_counts = {}

# Loop through each subdirectory (class) in the main dataset directory
for class_name in os.listdir(dataset_path):
    class_dir = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_dir):
        # Count the number of files (images) in the current class directory
        num_images = len([file for file in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, file))])
        class_counts[class_name] = num_images

# Sort the class counts by class name (optional, for better visualization)
class_counts = dict(sorted(class_counts.items()))

# Print the class counts
print("Number of images in each class:")
for class_name, count in class_counts.items():
    print(f'Class {class_name}: {count} images')

# Generate colors for each class
colors = plt.cm.tab10(np.linspace(0, 1, len(class_counts)))

# Plotting the data distribution
plt.figure(figsize=(12, 8))
bars = plt.bar(class_counts.keys(), class_counts.values(), color=colors)
plt.xlabel('Class')
plt.ylabel('Number of Images')
plt.title('Number of Images per Class')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Add counts on top of bars
for bar, count in zip(bars, class_counts.values()):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, count, ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
