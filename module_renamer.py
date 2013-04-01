import os
import shutil
import re
from string import capitalize as cap

class ModuleRenamer(object):

  def __init__(self, from_name, to_name, path_to_module = './'):
    self.from_name, self.to_name, self.path_to_module = from_name, to_name, path_to_module

  def validate_args(self):
    valid_name = '^[a-z][a-z0-9_]*$'
    return re.match(valid_name, self.from_name) and \
           re.match(valid_name, self.to_name) and \
           os.path.exists(self.path_to_module)

  def rename(self):
    new_module_dir = os.path.join(self.path_to_module, '..', self.to_name)

    if __debug__ and os.path.exists(new_module_dir):
      shutil.rmtree(new_module_dir)

    shutil.copytree(self.path_to_module, new_module_dir)

    for dirpath, dirnames, filenames in os.walk(new_module_dir):
      for filename in filenames:
        new_filename = re.sub(self.from_name, self.to_name, filename)
        file_path = os.path.join(dirpath, filename)
        new_file_path = os.path.join(dirpath, new_filename)
        shutil.move(file_path, new_file_path)
        print('\033[37m[mv]\033[0m ' + file_path + ' -> ' + new_file_path)
        self.rename_strings(new_file_path)

    print("Do not forget to rename those modules in the \033[35msystem\033[0m table.:")
    print("\033[33mUPDATE system SET filename = REPLACE(filename, '" + self.from_name + "', '" + self.to_name + "'), name = '" + self.to_name + "' WHERE name = '" + self.from_name + "';\033[0m")

  def rename_strings(self, filename):
    file = open(filename, 'r')
    content = file.read()
    content = self.replace_string(self.from_name, self.to_name, content)
    content = self.replace_string(cap(self.from_name), cap(self.to_name), content)
    file.close()

    file = open(filename, 'w')
    file.write(content)
    file.close()

  def replace_string(self, pattern, to, text):
    matches = re.findall('^.*' + pattern + '.*$', text, flags = re.M)
    if matches:
      for match in matches:
        print('\033[37m[sub]\033[0m ' + re.sub(pattern, "\033[31m" + to + "\033[0m", match))
    text = re.sub(pattern, to, text)
    return text
