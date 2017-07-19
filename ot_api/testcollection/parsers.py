def test_parser(row):
    return {
        'pk': row['id'],
        'name': row['name'],
    }
