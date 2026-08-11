import os
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Backgrounds
    content = content.replace('bg-[#FCFBF8]', 'bg-surface')
    content = content.replace('bg-[#F8F6F2]', 'bg-background')
    content = content.replace('bg-[#FCFBF8]/95', 'bg-surface/95')
    content = content.replace('bg-[#C0C6CC]/20', 'bg-primary/20')
    content = content.replace('bg-[#2563EB]', 'bg-gradient-to-r from-primary to-secondary text-white border border-white/10 shadow-lg shadow-primary/25')
    content = content.replace('hover:bg-[#1d4ed8]', 'hover:brightness-110')
    
    # Text
    content = content.replace('text-[#2B2F36]/70', 'text-text-secondary')
    content = content.replace('text-[#2B2F36]/80', 'text-text-secondary')
    content = content.replace('text-[#2B2F36]/60', 'text-text-muted')
    content = content.replace('text-[#2B2F36]', 'text-text-primary')
    content = content.replace('text-[#c0c6cc]', 'text-primary')
    content = content.replace('text-[#C0C6CC]', 'text-primary')
    content = content.replace('text-[#2563EB]', 'text-primary')
    content = content.replace('hover:text-[#2563EB]', 'hover:text-accent')
    content = content.replace('group-hover:text-[#2563EB]', 'group-hover:text-accent')
    content = content.replace('hover:text-[#2B2F36]', 'hover:text-text-primary')
    
    # Borders
    content = content.replace('border-[#E5E2DD]', 'border-border')
    content = content.replace('border-[#C0C6CC]', 'border-white/20')
    content = content.replace('hover:border-[#C0C6CC]', 'hover:border-white/20')
    
    # Focus
    content = content.replace('focus-visible:outline-[#2563EB]', 'focus-visible:outline-primary')
    content = content.replace('focus-visible:outline-blue-600', 'focus-visible:outline-primary')
    
    # Shadows
    content = content.replace('shadow-[0_12px_40px_rgba(43,47,54,0.04)]', 'shadow-lg shadow-black/50')
    content = content.replace('shadow-[0_8px_30px_rgb(0,0,0,0.04)]', 'shadow-lg shadow-black/50')
    content = content.replace('shadow-[0_10px_40px_rgb(0,0,0,0.05)]', 'shadow-lg shadow-black/50')
    content = content.replace('shadow-[0_4px_15px_rgba(37,99,235,0.15)]', 'shadow-lg shadow-primary/25')
    content = content.replace('shadow-[0_6px_20px_rgba(37,99,235,0.25)]', 'shadow-xl shadow-primary/40')
    content = content.replace('shadow-[0_4px_20px_rgba(37,99,235,0.2)]', 'shadow-xl shadow-primary/30')
    content = content.replace('shadow-[0_6px_25px_rgb(37,99,235,0.3)]', 'shadow-2xl shadow-primary/40')
    
    # Any other stragglers
    content = content.replace('hover:bg-blue-600', 'hover:brightness-110')
    content = content.replace('bg-white text-secondary', 'bg-surface text-text-primary')

    with open(filepath, 'w') as f:
        f.write(content)

for filepath in glob.glob('src/**/*.astro', recursive=True):
    process_file(filepath)

print("Hex replacement script executed.")
