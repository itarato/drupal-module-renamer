import os
import shutil

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

  def rename_file_names(self):
    new_module_dir = os.path.join(self.path_to_module, '..', self.to_name)

    if __debug__:
      # @todo remove after project complete
      if os.path.exists(new_module_dir):
        shutil.rmtree(new_module_dir)

    os.mkdir(new_module_dir)

    for dirpath, dirnames, filenames in os.walk(self.path_to_module):

      for subdirname in dirnames:
        os.mkdir(os.path.join(self.path_to_module, '..', self.to_name, subdirname))

      for filename in filenames:
        print('File: ' + os.path.join(dirpath, filename))

  def rename_strings(self):
    0
