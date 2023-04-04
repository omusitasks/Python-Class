# import sys
# import pandas as pd
# import numpy as np

# np.random.seed(56)


# def randdf(rows, cols):
#     df = pd.DataFrame(np.random.randint(0, 100, size=(rows, cols)))
#     return df

# print(randdf(4, 8))

import sys
import pandas as pd
import numpy as np

np.random.seed(56)

def randdf(rows, cols):
    df = pd.DataFrame(np.random.randint(0, 100, size=(rows, cols)))
    return df

if __name__ == "__main__":
    if len(sys.argv) == 3:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        print(randdf(rows, cols))