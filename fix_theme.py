import os
import re
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Fix broken replacements
    content = content.replace('text-text-text-primary', 'text-text-secondary')
    content = content.replace('text-text-text-muted', 'text-text-muted')
    
    # Replace remaining warm-off-white
    content = content.replace('bg-warm-off-white', 'bg-background')
    
    # Old hardcoded colors
    content = content.replace('bg-secondary text-white', 'bg-gradient-to-r from-primary to-secondary text-white shadow-lg shadow-primary/20 hover:shadow-primary/40 transition-all hover:scale-105')
    
    # bg-surface should have a subtle border
    # if it's bg-surface and doesn't have border-border or border-white/10, we could add it but let's just make sure border-primary/20 is border-white/10
    content = content.replace('border-primary/20', 'border-white/10')
    content = content.replace('border-border', 'border-white/10')
    
    # For badges and subtle backgrounds
    content = content.replace('bg-primary/10', 'bg-primary/20')
    content = content.replace('bg-primary/5', 'bg-primary/10')
    content = content.replace('text-primary', 'text-primary') # wait, text-primary in old theme was light silver. In new theme it's purple. That's fine.

    # Buttons
    # Hover states
    content = content.replace('hover:text-accent', 'hover:text-accent')
    content = content.replace('group-hover:text-accent', 'group-hover:text-accent')

    # Re-verify text-secondary didn't get messed up again
    # If there is any `text-secondary` left (the old dark charcoal), it should be text-text-primary
    content = re.sub(r'(?<!-)text-secondary(?!/)', 'text-text-primary', content)
    content = content.replace('text-secondary/70', 'text-text-secondary')
    content = content.replace('text-secondary/50', 'text-text-muted')
    content = content.replace('text-secondary/40', 'text-text-muted')
    content = content.replace('text-text-text-secondary', 'text-text-secondary')

    with open(filepath, 'w') as f:
        f.write(content)

for filepath in glob.glob('src/**/*.astro', recursive=True):
    process_file(filepath)

print("Theme fix script executed.")
