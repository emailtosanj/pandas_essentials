import pandas as pd



# data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
# person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})

def delete_duplicate_emails(person: pd.DataFrame) -> None:

    # Identify the email having dupe
    # Get the Id of the records
    # check which id is smaller
    # retain the one which is smaller
    person = person.sort_values(by=['id'], kind='mergesort')
    person = person.drop_duplicates(subset=['email'], keep='first')
    return person
