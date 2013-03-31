import os
import shutil
import re

class ModuleRenamer(object):

  from_name = ''
  to_name = ''
  path_to_module = ''

  def __init__(self, from_name, to_name, path_to_module = './'):
    super(ModuleRenamer, self).__init__()
    self.from_name = from_name
    self.to_name = to_name
    self.path_to_module = path_to_module

  def validate_args(self):
    # @todo Implement.
    return True

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
        self.rename_strings(new_file_path)

  def rename_strings(self, filename):
    0
