import csv
import pandas as pd
from functions import valid_options as v

choice = v.valid('[1] Start Purchases.',
        '[2] Inventory Management.',
        '[3] View Statistics.')


print(choice)
