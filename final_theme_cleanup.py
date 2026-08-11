import os
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Leftover text and backgrounds
    content = content.replace('text-warm-off-white', 'text-text-primary')
    content = content.replace('bg-white/50 backdrop-blur-sm', 'bg-white/5 backdrop-blur-md')
    content = content.replace('bg-white/80 backdrop-blur-md', 'bg-surface-elevated/80 backdrop-blur-md')
    
    # Leftover semantic classes from light theme
    # Using word boundaries for text-secondary
    import re
    content = re.sub(r'\btext-secondary\b', 'text-text-primary', content)
    content = re.sub(r'\bbg-secondary\b', 'bg-surface-elevated', content)
    content = re.sub(r'\bborder-secondary\b', 'border-primary', content)
    
    content = re.sub(r'\bbg-warm-off-white\b', 'bg-background', content)
    
    # Fix broken text-text-text
    content = content.replace('text-text-text-primary', 'text-text-secondary')
    content = content.replace('text-text-text-secondary', 'text-text-secondary')
    content = content.replace('text-text-text-muted', 'text-text-muted')
    
    with open(filepath, 'w') as f:
        f.write(content)

for filepath in glob.glob('src/**/*.astro', recursive=True):
    process_file(filepath)

print("Final cleanup script executed.")
