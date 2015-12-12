 #!/usr/bin/env python3

import os
import os.path
import random
import zipfile

class GenerateRandomData(object):
    """randomly generates a file of N bytes using the python 3.5 std library."""
    def __init__(self, amount_of_bytes, output_loc, file_name):
        super(GenerateRandomData, self).__init__()

        # Amount of bytes to be generated + location to store the file.
        self.change_amount_of_bytes (amount_of_bytes)
        self.change_output_location (output_loc)
        self.change_output_file_name (file_name)

        self.rand_content = bytes()

    ###                    ---             ###
    ### "getters/setters" functions below  ###
    ###                    ---             ###

    def change_output_location(self, new_location):
        self.output_location = new_location

    def change_output_file_name(self, new_name, prefix="ds-", postfix=""):
        self.file = "".join([prefix, new_name, postfix])

    def change_amount_of_bytes(self, amount):
        self.n_bytes = amount

    def get_full_file_path(self):
        return "/".join([self.output_location, self.file])

    def get_output_location(self):
        return self.output_location

    def get_output_file_name(self):
        return self.file

    ###            ---              ###
    ### "generate" functions below  ###
    ###            ---              ###

    def generate_bytes(self, x_amount=128, stdout_print=False):
        """
        Generates for amount=n_bytes random contents.
        This is splitted in x byte writes (purpose: not overloading memory)

        TODO{foresterre}: Currently just returns all bytes at once (thus not like written above).

        """
        rand = self.generate_per_x_bytes(amount=self.n_bytes)

        if stdout_print:
            print(rand)
        # left = self.n_bytes
        # parts = self.n_bytes/x_amount

        # for i in range(0, parts):
            # yield rand

        self.rand_content = rand


    def generate_per_x_bytes(self, amount=128):
        return os.urandom(amount)

    ###            ---            ###
    ### "write" functions below   ###
    ###            ---            ###

    def write_file(self):
        """
        Writes the random content to a file.

        TODO{foresterre}: This needs some more love.

        TODO{foresterre}: sequentially write (like a stream).
        TODO{foresterre}: Otherwise memory overflow might occur.

        """
        loc = self.get_full_file_path()

        with open(loc, mode="wb+") as f:
            f.write(self.rand_content)


    def safe_write(self):
        """
        Safe write:
        1. creates a new file
        2. writes contents to new file
        3. tries to move new file to the target ouput location (thus replacing a possible existing older copy; if the move is possible)

        """
        pass

    def clean(self):
        """
        Cleans the given target location (by rewriting 0-bytes to the file).
        """
        loc = self.get_full_file_path()

        with open(loc, mode="wb+") as f:
            f.write(b"")


    ###            ---            ###
    ### "Amount" functions below  ###
    ###            ---            ###
    
    # TODO{foresterre}: use these in the methods above
    
    def bytes(self, amount_of_bytes):
        return amount_of_bytes

    def kilobytes(self, amount_of_bytes):
        return amount_of_bytes * 1000

    def kibibytes(self, amount_of_bytes):
        return amount_of_bytes * 1024

    def megabytes(self, amount_of_bytes):
        return amount_of_bytes * 1000**2

    def mebibytes(self, amount_of_bytes):
        return amount_of_bytes * 1024**2

    def gigabytes(self, amount_of_bytes):
        return amount_of_bytes * 1000**3

    def gibibytes(self, amount_of_bytes):
        return amount_of_bytes * 1024**3



if __name__ == '__main__':

    gen = GenerateRandomData(0, "D:/", "$__default__")

    # Zip file name
    fid = random.randint(100, 999)
    zip_target_file = "".join(["data", "-", str(fid), ".zip"])

    # Store all files in a zip (just to group them in one file)
    zipper = zipfile.ZipFile("".join([gen.output_location, "/", zip_target_file]), "w")

    # Generate this amount of files with random data
    gen_this_amount_of_files = 100
    gen_file_extension = ".rgd"

    # For each:
    #   Generate the random file
    #   Write the random file to the zip grouper
    #   Zero out the generated random file (not delete)
    for i in range(0, gen_this_amount_of_files):
        rng = random.randint(1000, 99999)
        print("progress: ", i+1, "/", gen_this_amount_of_files, " size=", rng, sep="")
        gen.change_output_file_name("".join([str(rng) , gen_file_extension]))
        gen.change_amount_of_bytes(gen.kibibytes(rng))
        gen.generate_bytes(stdout_print=False)
        gen.write_file()

        zipper.write(gen.get_full_file_path(), gen.get_output_file_name(), zipfile.ZIP_DEFLATED)

        gen.clean()

    # Clean up the residual zero-ed out generated random files.
    # WARNING: removes all files with a certain extension!
    # TODO{foresterre}: This can be done cleaner :)
    remove_files = [i for i in os.listdir(gen.get_output_location()) if i.endswith(gen_file_extension)]

    for i in remove_files:
        print("removing: ", i)
        os.remove("/".join([gen.get_output_location(), i]))




