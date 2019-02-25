# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Python (jupyter virtualenv)
#     language: python
#     name: jupyter
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
# ---

# +
# the proportion of actual positives that are correctly identified as such
sensitivity = 0.86
# the proportion of actual negatives that are correctly identified as such 
specificity = 0.33
n = 10000
prevalence = 172.6/100000
mortality = 47.2/100000

########

affected = prevalence * n
not_affected = n - affected
deaths_without_treatment = mortality * n

#########

true_positive = round(sensitivity * affected)
false_negative = round(affected - true_positive)
true_negative = round(specificity * not_affected)
false_positive = round(not_affected - true_negative)

print(true_positive, false_negative, true_negative, false_positive)
# -

treatment_cure_rate = 0.89
treatment_harm_rate = 0.01
treatment_mortality_rate = 0.0001
print("Of {:.0f} deaths without treatment, {:.0f} extra people would be cured, {:.0f} people would be harmed, {:.0f} extra people would die".format(
    deaths_without_treatment, 
    (treatment_cure_rate * true_positive * mortality / prevalence),
    treatment_harm_rate * false_positive  + treatment_harm_rate * true_positive,
    treatment_mortality_rate * false_positive + treatment_mortality_rate * true_positive
))
