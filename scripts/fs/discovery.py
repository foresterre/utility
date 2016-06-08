import os

class Discovery(object):

    def __init__(self, location):
        self.location = location

        self.file_list = []

    def discover(self):
        self._run()
        return self.file_list

    def get(self):
        return self.file_list

    def _run(self):
        """
        Finds files at the specified location.
        
        Does not:
            *   List empty folders

        :return: The instance variable, file_list, after listing all files in the given path.
        """

        for dir_path, dir_names, file_names in os.walk(self.location):

            clean_dir_path = os.path.realpath(dir_path)
            for file_path in file_names:
                self.file_list.append(os.path.join(clean_dir_path, file_path))


    def __repr__(self):
        return "Discovery[location={}]".format(self.location)
