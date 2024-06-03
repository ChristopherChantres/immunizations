'''
Return a tuple:
 - Average number of influenza vacc for those who received breastmilk
 - Average number of influenza vacc for those who did NOT received breastmilk
 
 Return --> (yes, no)
 
    (total number of influenza vacc) / (total number of babies with breaskmilk)
    (total number of influenza vacc) / (total number of babies without breaskmilk)

    1 indicates "Yes"
    2 indicates "No"
    77 indicates "Don’t know"
    99 could be used to represent "Missing" (assuming from the context)
    NaN represents missing data
'''
import pandas as pd

def average_influenza_doses():
    file_path = 'NISPUF17.csv'
    breasted_babies_code = 'CBF_01'
    influenza_vacc_code = 'P_NUMFLU'

    # Load the dataset
    df = pd.read_csv(file_path)

    # Filter the DataFrame for breastfed and non-breastfed children
    breasted_df = df[df[breasted_babies_code] == 1]
    not_breasted_df = df[df[breasted_babies_code] == 2]

    # Calculate the average number of influenza vaccines, excluding NaN values by default
    avg_vaccines_breastfed = breasted_df[influenza_vacc_code].mean()
    avg_vaccines_not_breastfed = not_breasted_df[influenza_vacc_code].mean()

    return (avg_vaccines_breastfed, avg_vaccines_not_breastfed)


if __name__ == '__main__':
    test = average_influenza_doses()
    print(test)
    assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."