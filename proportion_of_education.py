import pandas as pd

def proportion_of_education():
    file_path = 'NISPUF17.csv'

    df = pd.read_csv(file_path)
    education_counts = df['EDUC1'].value_counts()
    total_count = education_counts.sum()
    cat4, cat3, cat2, cat1 = education_counts.array

    # Calculatin each percentage from the total
    ptge_cat4 = cat4 / total_count
    ptge_cat3 = cat3 / total_count
    ptge_cat2 = cat2 / total_count
    ptge_cat1 = cat1 / total_count

    result = {
        'less than high school': ptge_cat1,
        'high school': ptge_cat2,
        'more than high school but not college': ptge_cat3,
        'college': ptge_cat4
    }

    return result

if __name__ == '__main__':
    data = proportion_of_education()
    print(data)

    # Code Operation Validation
    assert type(proportion_of_education())==type({}), "You must return a dictionary."
    assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
    assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
    assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
    assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
    assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
