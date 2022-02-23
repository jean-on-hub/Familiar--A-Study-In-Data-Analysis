# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
# inspecting data
print(lifespans.head())
# getting vein data
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == "vein"]
# print(vein_pack_lifespans)
# get mean
vpl_mean = np.mean(vein_pack_lifespans)
print(vpl_mean)
# running a one sample ttest to check average lifespan association with 73
ans1,pvalue = ttest_1samp(vein_pack_lifespans,73)
print(pvalue)
# with our p value being significantly less than 0.05 we can say The average lifespan of a Vein Pack subscriber is NOT 73 years
# getting artery data
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == "artery"]
# print(artery_pack_lifespans)
# get mean
apl_mean = np.mean(artery_pack_lifespans)
# print(apl_mean)

# using a two sample test We’d like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy for the Artery Pack
ans1,pvalue = ttest_ind(artery_pack_lifespans,vein_pack_lifespans)
print(pvalue)
# with 0.05 as  significance threshold we can say The average lifespan of a Vein Pack subscriber is equal to the average lifespan of an Artery Pack subscriber.
# analysing iron data
print(iron.head())
# using chisquare We’d like to find out if there is a significant association between which pack (Vein vs. Artery) someone subscribes to and their iron level.
Xtab = pd.crosstab(iron.pack,iron.iron)

chi2,pval,df,expected = chi2_contingency(Xtab)

print(pval)







