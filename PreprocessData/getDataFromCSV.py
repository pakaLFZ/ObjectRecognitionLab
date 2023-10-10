
def getDataFromCSV(table, apple):
    apple_data = table.loc[table['filename'] == apple].values.tolist()
    if apple_data:
        # skip the first value (apple)
        return apple_data[0][1:]

    return None