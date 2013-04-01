import sys
from module_renamer import ModuleRenamer

if __name__ == '__main__':
  if len(sys.argv) < 4:
    print("Argument error. Syntax:\n$ python -O rename.py NAME_FROM NAME_TO PATH_TO_MODULE")
    sys.exit(1)

  print("Rename from \033[35m" + sys.argv[1] + "\033[0m to \033[35m" + sys.argv[2] + "\033[0m in \033[35m" + sys.argv[3] + "\033[0m.")

  renamer = ModuleRenamer(sys.argv[1], sys.argv[2], sys.argv[3])

  if not renamer.validate_args():
    print("Argument error. Names should be valid PHP function literals. Path should exist.")
    sys.exit(1)

  renamer.rename()
