import exiftool
import config

def get_exiftool_metadata(file_path):

    with exiftool.ExifToolHelper(executable=config.EXIFTOOL_PATH) as et: #et = exiftool.ExifToolHelper() creates session, the with is for closing it after using the session

        metadata = et.get_metadata(
            str(file_path)
        )[0] #get_metadata --> returns list [{..}], the [0] means first of the array --> {..}

    return metadata