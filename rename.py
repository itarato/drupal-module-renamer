import sys

def rename_file_names():
  null

def rename_strings():
  null

if __name__ == '__main__':
  print("Drupal Module Renamer")

  if len(sys.argv) < 4:
    print("Argument error. Syntax:\n$ python rename.py NAME_FROM NAME_TO PATH_TO_MODULE")
    sys.exit(1)

  print("Rename from " + sys.argv[1] + " to " + sys.argv[2] + " in " + sys.argv[3])
