import unittest
import h1b

data1 = [['', 'CASE_STATUS', 'DECISION_DATE', 'VISA_CLASS', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WORKSITE_STATE', 'SOC_NAME'],
        ['0', 'CERTIFIED', '2018-01-29', 'H-1B','REDMOND', 'WA', 'WA', 'SOFTWARE ENGINEER'],
        ['1', 'CERTIFIED', '2018-02-19', 'H-1B','REDMOND', 'CA', 'CA', 'DATABASE ADMINISTRATOR'],
        ['2', 'CERTIFIED', '2018-02-19', 'H-1B','REDMOND', 'WA', 'PA', 'SOFTWARE ENGINEER'],
        ['3', 'CERTIFIED', '2018-02-22', 'H-1B','REDMOND', 'WA', 'PA', 'TAX SENIOR'],
        ['4', 'CERTIFIED', '2018-03-02', 'H-1B','REDMOND', 'CA', 'CA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['5', 'CERTIFIED', '2018-03-09', 'H-1B','REDMOND', 'WA', 'PA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['6', 'CERTIFIED', '2018-03-14', 'H-1B','REDMOND', 'MI', 'MI', 'SOFTWARE ENGINEER'],
        ['7', 'DENIED', '2018-03-15', 'H-1B','REDMOND', 'OH', 'OH', 'SOFTWARE ENGINEER']]

data2 = [['', 'CASE_STATUS', 'DECISION_DATE', 'VISA_CLASS', 'EMPLOYER_CITY', 'WORKSITE_STATE', 'EMPLOYER_STATE', 'SOC_NAME'],
        ['0', 'CERTIFIED', '2018-01-29', 'H-1B','REDMOND', 'WA', 'WA', 'SOFTWARE ENGINEER'],
        ['1', 'CERTIFIED', '2018-02-19', 'H-1B','REDMOND', 'CA', 'CA', 'DATABASE ADMINISTRATOR'],
        ['2', 'CERTIFIED', '2018-02-19', 'H-1B','REDMOND', 'PA', 'PA', 'SOFTWARE ENGINEER'],
        ['3', 'CERTIFIED', '2018-02-22', 'H-1B','REDMOND', 'PA', 'PA', 'TAX SENIOR'],
        ['4', 'CERTIFIED', '2018-03-02', 'H-1B','REDMOND', 'CA', 'CA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['5', 'CERTIFIED', '2018-03-09', 'H-1B','REDMOND', 'PA', 'PA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['6', 'CERTIFIED', '2018-03-14', 'H-1B','REDMOND', 'MI', 'MI', 'SOFTWARE ENGINEER'],
        ['7', 'DENIED', '2018-03-15', 'H-1B','REDMOND', 'OH', 'OH', 'SOFTWARE ENGINEER']]

data11 = [['CASE_STATUS', 'VISA_CLASS','WORKSITE_STATE', 'SOC_NAME'],
        ['CERTIFIED', 'H-1B', 'WA', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'CA', 'DATABASE ADMINISTRATOR'],
        ['CERTIFIED', 'H-1B', 'PA', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'PA', 'TAX SENIOR'],
        ['CERTIFIED', 'H-1B', 'CA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['CERTIFIED', 'H-1B', 'PA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['CERTIFIED', 'H-1B', 'MI', 'SOFTWARE ENGINEER'],
        ['DENIED', 'H-1B', 'OH', 'SOFTWARE ENGINEER']]

filters = ['CASE_STATUS','VISA_CLASS','WORKSITE_STATE','SOC_NAME']

data21 = [['CASE_STATUS', 'VISA_CLASS','WORKSITE_STATE', 'SOC_NAME'],
        ['CERTIFIED', 'H-1B', 'WA', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'CA', 'DATABASE ADMINISTRATOR'],
        ['CERTIFIED', 'H-1B', 'PA', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'PA', 'TAX SENIOR'],
        ['CERTIFIED', 'H-1B', 'CA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['CERTIFIED', 'H-1B', 'PA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['CERTIFIED', 'H-1B', 'MI', 'SOFTWARE ENGINEER']]

rank1 = [['SOFTWARE ENGINEER', '3', 3/7],
         ['COMPUTER OCCUPATIONS, ALL OTHER', '2', 2/7], 
         ['DATABASE ADMINISTRATOR', '1', 1/7], 
         ['TAX SENIOR', '1', 1/7]]

rank2 = [['PA', '3', 3/7], ['CA', '2', 2/7], ['MI', '1', 1/7], ['WA', '1', 1/7]]

data22 = [['CASE_STATUS', 'VISA_CLASS','WORKSITE_STATE', 'SOC_NAME'],
        ['CERTIFIED', 'H-1B', 'DE', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'CA', 'DATABASE ADMINISTRATOR'],
        ['CERTIFIED', 'H-1B', 'PA', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'PA', 'TAX SENIOR'],
        ['CERTIFIED', 'H-1B', 'AL', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['CERTIFIED', 'H-1B', 'TX', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['CERTIFIED', 'H-1B', 'MD', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'NJ', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'GA', 'COMPUTER OCCUPATIONS, ALL OTHER'],
        ['CERTIFIED', 'H-1B', 'WA', 'SOFTWARE ENGINEER'],
        ['CERTIFIED', 'H-1B', 'OH', 'SOFTWARE ENGINEER']]

rank3 = [['PA', '2', 2/11], ['AL', '1', 1/11], ['CA', '1', 1/11], ['DE', '1', 1/11],
         ['GA', '1', 1/11], ['MD', '1', 1/11], ['NJ', '1', 1/11], ['OH', '1', 1/11],
         ['TX', '1', 1/11], ['WA', '1', 1/11]]

class TestStringMethods(unittest.TestCase):
    def test_column_select1(self):
        self.assertEqual(h1b.column_select(data1,filters),data11)

    def test_column_select2(self):
        # column order changes
        self.assertEqual(h1b.column_select(data2, filters), data11)

    def test_certified1(self):
        self.assertEqual(h1b.certified_records(data11), data21)

    def test_rank1(self):
        self.assertEqual(h1b.get_rank(data21, target = 'SOC_NAME'), rank1)

    def test_rank2(self):
        self.assertEqual(h1b.get_rank(data21, target = 'WORKSITE_STATE'), rank2)

    def test_rank3(self):
        self.assertEqual(h1b.get_rank(data22, target = 'WORKSITE_STATE'), rank3) 

if __name__ == '__main__':
    unittest.main()