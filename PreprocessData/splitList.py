def splitList(input_list, chunk_size=2500):
    """
    Split a list into smaller lists of the specified chunk size.
    :param input_list: The list to be split.
    :param chunk_size: The desired length of each smaller list.
    :return: A list of smaller lists.
    """
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]
