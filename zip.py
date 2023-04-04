import zipfile




'''def create_zip(filepaths, folder):
    zip_file_path = folder + '.zip'

    with zipfile.ZipFile(zip_file_path, 'w') as file:
        for filepath in filepaths:
            file.write(filepath) '''


def create_zip(filepaths, folder):
    zip_file_path = folder + ".zip"

    with zipfile.ZipFile(zip_file_path, 'w') as file:
        for filepath in filepaths:
            file.write(filepath)







