import sys
import wget

for arg in sys.argv:
    print(arg)

filename = wget.download("http://www.vim.org/scripts/download_script.php?src_id=9750")
print(" -> "+ filename)
