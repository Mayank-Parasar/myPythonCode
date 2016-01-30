# This replaces all 'equalwidth' with 'equalbisection' in any non-hidden file in the current directory

import os
[os.rename(f, f.replace('equalwidth', 'equalbisection')) for f in os.listdir('.') if not f.startswith('.')]
