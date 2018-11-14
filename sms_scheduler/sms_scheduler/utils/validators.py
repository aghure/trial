def valid_datetime_type(arg_datetime_str):
    """custom argparse type for user datetime values given from the command line"""
    try:
        return datetime.datetime.strptime(arg_datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        msg = "Given Datetime ({0}) not valid! Expected format, 'YYYY-MM-DD HH:mm'!".format(arg_datetime_str)
        raise argparse.ArgumentTypeError(msg)


def valid_file_path(arg_file_path):
    """custom argparse type for validating csv file path"""
    try:
        return os.stat(arg_file_path)
    except os.error:
        msg = "Given file path is not exits! ({0})".format(arg_file_path)
        raise argparse.ArgumentTypeError(msg)
    except Exception as e:
        msg = "there is some problem with file"
        raise argparse.ArgumentTypeError(msg)



