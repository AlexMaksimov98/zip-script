from zipfile import ZipFile


def compare_two_zip(first, second):
    # Try to execute the script. We are catching an exception if the file doesn't exist
    try:
        # Reading the first .zip
        with ZipFile(first, 'r') as first:
            first_zip = first.namelist()
        # Reading the second .zip
        with ZipFile(second, 'r') as second:
            second_zip = second.namelist()
        # Using list comprehension to create identical elements and unique elements in both zip files.
        identical_list = [i for i, j in zip(first_zip, second_zip) if i == j]
        first_unique_list = [i for i in first_zip if i not in second_zip]
        second_unique_list = [j for j in second_zip if j not in first_zip]
        # Creating beautiful messages
        identical_names = '\n   '.join(identical_list)
        first_unique_names = '\n   '.join(first_unique_list)
        second_unique_names = '\n   '.join(second_unique_list)
        # Building a message
        message = f'Identical\n   {identical_names}\n' \
                  f'Unique in first.zip\n   {first_unique_names}\n' \
                  f'Unique in second.zip\n   {second_unique_names}'
        # Printing message to the console
        print(message)
    except FileNotFoundError:
        print('There is no such file.')


compare_two_zip('first.zip', 'second.zip')
