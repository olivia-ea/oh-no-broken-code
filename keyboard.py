
def assign_cat_to_instrument(cat_lst, instrument_lst):
    return dict(zip(cat_lst, instrument_lst))

def print_assigment(zipped_dict):
    result = []
    for key, value in zipped_dict.items():
        result.append(f"{key} plays the {value}!")
    return result

if __name__ == '__main__':
    cats = ['Grizabella', 'Rum Tum Tugger', 'Demeter', 'Munkustrap',
            'Mistoffelees', 'Macavity', 'Rumpleteazer', 'Mungo Jerry', 'Skimbleshanks']
    instruments = ['keyboard', 'cello', 'bass', 'flute', 'pipe', 'piano',
                   'violin', 'oboe', 'triangle']
    cat_instrument_dict = assign_cat_to_instrument(cats, instruments)
    print(cat_instrument_dict)

    result_dict = print_assigment(cat_instrument_dict)
    for item in result_dict:
        print(item)
