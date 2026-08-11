import os
import re
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Colors
    content = content.replace('bg-warm-off-white', 'bg-background')
    content = content.replace('text-secondary/70', 'text-text-secondary')
    content = content.replace('text-secondary/50', 'text-text-muted')
    content = content.replace('text-secondary/40', 'text-text-muted')
    content = content.replace('text-secondary', 'text-text-primary')
    content = content.replace('border-primary/20', 'border-border')
    content = content.replace('border-primary/10', 'border-border')
    content = content.replace('border-primary/40', 'border-border')
    content = content.replace('border-secondary', 'border-primary')
    content = content.replace('bg-primary/5', 'bg-border')
    content = content.replace('bg-primary/10', 'bg-border/50')
    content = content.replace('bg-accent/5', 'bg-primary/10')
    content = content.replace('bg-accent/10', 'bg-primary/20')
    
    # Primary Buttons
    # Previous primary buttons were typically: bg-secondary text-white
    # We replace them with the galaxy gradient
    content = re.sub(
        r'bg-secondary\s+text-white',
        'bg-gradient-to-r from-primary to-secondary hover:from-secondary hover:to-accent text-white shadow-lg shadow-primary/25 border border-white/10',
        content
    )
    # If there are any leftover bg-secondary (not buttons), make them surface-elevated
    content = content.replace('bg-secondary', 'bg-surface-elevated')

    # Update global gradients (blur blobs)
    content = content.replace('bg-primary/5 blur-[120px]', 'bg-primary/20 blur-[120px]')
    content = content.replace('bg-accent/5 blur-[100px]', 'bg-accent/20 blur-[100px]')

    # Form inputs
    content = content.replace('bg-warm-off-white border-2 border-primary/10', 'bg-surface border-2 border-border')
    content = content.replace('focus:border-accent/40 focus:ring-accent/10', 'focus:border-primary/50 focus:ring-primary/20')

    with open(filepath, 'w') as f:
        f.write(content)

for filepath in glob.glob('src/**/*.astro', recursive=True):
    process_file(filepath)

print("Theme replacement script executed.")
