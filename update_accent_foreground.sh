#!/bin/bash
# update global.css to add accent-foreground and primary-foreground
sed -i 's/--color-accent-pink: #EC4899;/--color-accent-pink: #EC4899;\n    --color-primary-foreground: #FFFFFF;\n    --color-secondary-foreground: #FFFFFF;\n    --color-accent-foreground: #082F49;/' src/styles/global.css
sed -i 's/--color-accent-pink: #EC4899;/--color-accent-pink: #EC4899;\n    --color-primary-foreground: #FFFFFF;\n    --color-secondary-foreground: #FFFFFF;\n    --color-accent-foreground: #082F49;/' src/styles/global.css
# wait, I need to do it correctly for light and dark
