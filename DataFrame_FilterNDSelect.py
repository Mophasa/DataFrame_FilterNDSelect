### Filtrage et sélection de trames de données à l’aide d’iloc et loc

#1. Importer pandas et créer la trame de données
import pandas as pd

data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Gender': ['Mâle', 'Femelle', 'Mâle', 'Femelle', 'Mâle', 'Femelle'],
    'Salaire': [50000, 60000, 45000, 55000, 70000, 55000],
    'Expérience': [3, 7, 2, 5, 10, 4]
}

employee_df = pd.DataFrame(data)

#2. Sélectionner les "3" premières lignes avec iloc
premieres_lignes = employee_df.iloc[:3]
print(premieres_lignes)

#3. Sélectionner toutes les lignes où le département est « Marketing » avec loc
marketing_employees = employee_df.loc[employee_df['Department'] == 'Marketing']
print(marketing_employees)

#4. Sélectionner les colonnes Age et Gender pour les 4 premières lignes avec iloc
age_gender = employee_df.iloc[:4, [2, 3]]
print(age_gender)

#5. Sélectionner les colonnes Salaire et Expérience pour toutes les lignes où le sexe est « Mâle » avec loc
male_salary_experience = employee_df.loc[employee_df['Gender'] == 'Mâle', ['Salaire', 'Expérience']]
print(male_salary_experience)