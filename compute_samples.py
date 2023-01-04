import numpy as np
import pandas as pd
from chow_ff_lp3 import chow_ff_lp3

victoria   = pd.read_csv('./victoria.txt',header=None,sep=' ')[1].values.astype('float32')
mt_carmel  = pd.read_csv('./mt_carmel.txt',skiprows=72,sep='\t')[1:]['peak_va'].values.astype('float32')
whitesburg = pd.read_csv('./whitesburg.txt',skiprows=72,sep='\t')[1:]['peak_va'].values.astype('float32')
whitesburg = whitesburg[~np.isnan(whitesburg)]

print('\t\t5 years\t50 years')
print('Victoria, TX\t'+str(np.round(chow_ff_lp3(victoria,5),0).astype('int64'))+'\t'+str(np.round(chow_ff_lp3(victoria,50),0).astype('int64')))
print('Mt Carmel, IL\t'+str(np.round(chow_ff_lp3(mt_carmel,5),0).astype('int64'))+'\t'+str(np.round(chow_ff_lp3(mt_carmel,50),0).astype('int64')))
print('Whitesburg, AL\t'+str(np.round(chow_ff_lp3(whitesburg,5),0).astype('int64'))+'\t'+str(np.round(chow_ff_lp3(whitesburg,50),0).astype('int64')))

