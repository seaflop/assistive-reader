"""
The class in this file is used for basic file management operations.
It allows for easy creation of paths (with or without confirmation),
and shifting files within a directory.
"""
import os

class FileManager():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_path(self, *paths: str):
        for path in paths:
            # Make sure that path is a string
            assert isinstance(path, str), "path must be a string!"
            os.makedirs(path, exist_ok=True)

    def create_path_with_confirmation(self, path: str):
        print(f"Cannot find an existing directory at {path}.\nCreate it?")
        confirm_create_directory = str(input("y or n: "))
        if (confirm_create_directory.lower() == "y"):
            self.create_path(path)
        else:
            raise OSError(f"{path=} cannot be found!")
        return

    """
        The below function shifts files and renames them to open space
        for a new file.
        Takes a parameter for the directory we wish to perform the shift in,
        the base name of the file that we wish to perform actions on, and the
        maximum number of those files we want to keep.
        e.g. 
            directory = ./testing
            base_name = test.txt
            max_num_of_files = 4

            ./testing/test5.txt -> deleted
            ./testing/test4.txt -> deleted
            ./testing/test3.txt -> test4.txt
            ./testing/hello.wav -> unaffected
            ./testing/test2.txt -> test3.txt
            ./testing/test.py   -> unaffected
            ./testing/test.txt  -> unaffected
            ./testing/test1.txt -> test2.txt

            This allows us to create a new test1.txt elsewhere in the program 
            and not overwrite any old files.
        
        By default checks in the project folder directory and only allows for
        one file of the base_name type.
    """
    def make_space_for_file(self, file_location: str, max_num_of_files = 1):
        # Make sure that file_location is a string
        assert isinstance(file_location, str), "file_location must be a string!"

        # Split file_location into directory_name and file_name
        directory_name, file_name = os.path.split(file_location)

        # Check that directory_name exists. If not, create it with confimation.
        if (not os.path.exists(directory_name)):
            self.create_path_with_confirmation(directory_name)

        # Make sure that file_name contains a "1"
        assert "1" in file_name, "incorrect formatting for file_location!"

        # Make sure that max_num_of_files is an integer
        assert isinstance(max_num_of_files, int), "max_num_of_files must be an integer!"

        # Split the file_name at the last occurrence of "1"
        parts = file_name.rsplit("1", 1)

        # Shift files up 
        for index in range(max_num_of_files, 1, -1):
            if (os.path.isfile(
                file_location:= os.path.join(
                    directory_name, f"{parts[0]}{index - 1}{parts[1]}")
                )
            ):
                os.rename(file_location, os.path.join(directory_name, f"{parts[0]}{index}{parts[1]}"))

        # Shift files down in case we already have space
        # First make sure the directory isn't empty and then find the lowest file location 
        lowest_file_num = 1
        while (not os.path.isfile(
            os.path.join(
                directory_name, f"{parts[0]}{lowest_file_num}{parts[1]}")
            ) and len(os.listdir(directory_name)) != 0
        ):
            lowest_file_num += 1
        # Then we shift the files down
        for index in range(2, max_num_of_files):
            if (lowest_file_num > 2):
                os.rename(
                    os.path.join(
                        directory_name, f"{parts[0]}{lowest_file_num}{parts[1]}"), 
                    os.path.join(
                        directory_name, f"{parts[0]}{index}{parts[1]}"))
                lowest_file_num += 1
            #os.rename()

        # Delete extra files
        highest_file_num = max_num_of_files
        # Here we just keep checking if any files above the max_num_of_files exist and delete them
        while (os.path.isfile(
            highest_file_location := os.path.join(
                directory_name, f"{parts[0]}{highest_file_num + 1}{parts[1]}")
            )
        ):
            os.remove(highest_file_location)
            highest_file_num += 1


        return

if __name__ == "__main__":
    fm = FileManager()
    fm.make_space_for_file("./ocr/ocr1.txt", 3)
