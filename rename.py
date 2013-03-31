import sys
from module_renamer import ModuleRenamer

if __name__ == '__main__':
  print("Drupal Module Renamer")

  if len(sys.argv) < 4:
    print("Argument error. Syntax:\n$ python -O rename.py NAME_FROM NAME_TO PATH_TO_MODULE")
    sys.exit(1)

  print("Rename from " + sys.argv[1] + " to " + sys.argv[2] + " in " + sys.argv[3])

  renamer = ModuleRenamer(sys.argv[1], sys.argv[2], sys.argv[3])

  if not renamer.validate_args():
    print("Argument error.")
    sys.exit(1)

  renamer.rename()
