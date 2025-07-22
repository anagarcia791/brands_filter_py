from db_checker import (checking_syntactic_similarity, checking_phonetic_similarity,
                        mean_value_calculation, risk_perception)
from db_cleaning import (copy_excel_file, db_cleaning,
                         db_filtering_by_sign_type_and_status, db_filtering_by_syntactic_and_phonetic_similarity,
                         db_filtering_by_mean_value_between_50_and_60, final_filter)

brand_to_compare = 'CLASTOZ'
original_file = 'CLASTOZ.xlsx'
backup_file = f'_FILTER_BY_BRAND_RESULT_{brand_to_compare}.xlsx'

# Create backup copy
copy_excel_file(original_file, backup_file)
# Cleaning
db_cleaning(backup_file, backup_file)
# Filtering by sign type and status
db_filtering_by_sign_type_and_status(backup_file, 'Marca', 'Registrada')
# Syntactic similarity calculation
checking_syntactic_similarity(backup_file, brand_to_compare)
# Syntactic phonetic calculation
checking_phonetic_similarity(backup_file, brand_to_compare)
# Mean value calculation
mean_value_calculation(backup_file)
# Risk perception calculation
risk_perception(backup_file)
# Filtering db by mean value between 50 and 60
db_filtering_by_mean_value_between_50_and_60(backup_file)
# Filtering by syntactic and phonetic similarity
db_filtering_by_syntactic_and_phonetic_similarity(backup_file, brand_to_compare)
# Filtering by syntactic and phonetic similarity
final_filter(backup_file, brand_to_compare)