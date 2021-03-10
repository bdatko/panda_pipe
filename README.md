[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://github.com/commitizen-tools/commitizen) [![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pandas_pipe) ![PyPI](https://img.shields.io/pypi/v/pandas_pipe)
## Install
```pip install pandas_pipe```
## Purpose
* a collection of pandas DataFrame methods and functions I commonly used decorated with [scikit-lego](https://scikit-lego.readthedocs.io/en/latest/index.html)'s `@log_step` to enable logging within method chaining
* Wanted to use the logging of common pandas methods across projects
* Inspired from Vincent D. Warmerdam's PyData Eindhoven 2019 talk titled [Untitled12.ipynb](https://www.youtube.com/watch?v=yXGCKqo5cEY)
* See the [docs for pandas pipelines of scikit-lego](https://scikit-lego.readthedocs.io/en/latest/pandas_pipeline.html) to view the general use case for `@log_step`
*  See `examples/demo.ipynb` for a few workflows and links to other relevant SE questions
```python
In [1]: import pandas as pd; import numpy as np; import logging

In [2]: import pandas_pipe

In [3]: stream_handler = logging.StreamHandler()

In [4]: pandas_pipe.logger.addHandler(stream_handler)

In [5]: dataf_input = pd.DataFrame(
   ...:     {
   ...:         "aaa": {0: 10, 1: 11, 2: 12, 3: 13},
   ...:         "myid": {0: 1, 1: 2, 2: 3, 3: 4},
   ...:         "num": {0: "1, 2, 3", 1: np.nan, 2: "1, 2", 3: np.nan},
   ...:         "text": {0: "aa, bb, cc", 1: np.nan, 2: "cc, dd", 3: "ee"},
   ...:         "states": {
   ...:             0: "Wyoming; Illinois; New Hampshire",
   ...:             1: "Pennsylvania",
   ...:             2: "New York",
   ...:             3: "Pennsylvania",
   ...:         },
   ...:     }
   ...: )

In [6]: dataf_input
Out[6]: 
   aaa  myid      num        text                            states
0   10     1  1, 2, 3  aa, bb, cc  Wyoming; Illinois; New Hampshire
1   11     2      NaN         NaN                      Pennsylvania
2   12     3     1, 2      cc, dd                          New York
3   13     4      NaN          ee                      Pennsylvania

In [7]: (
   ...:     dataf_input.pipe(pandas_pipe.start_pipeline)
   ...:     .pipe(pandas_pipe.explode_setup, columns=["num", "text"], delimiter=",")
   ...:     .pipe(pandas_pipe.explode_setup, columns=["states"], delimiter=";")
   ...:     .pipe(pandas_pipe.explode, column="num", ignore_index=False)
   ...:     .pipe(pandas_pipe.explode, column="text", ignore_index=False)
   ...:     .pipe(pandas_pipe.explode, column="states", ignore_index=False)
   ...:     .pipe(pandas_pipe.drop_duplicates)
   ...: )
[start_pipeline(df)] time=0:00:00.000152 n_obs=4, n_col=5 names=['aaa', 'myid', 'num', 'text', 'states']
[explode_setup(df, columns = ['num', 'text'], delimiter = ',')] time=0:00:00.001107 n_obs=4, n_col=5 delta=(0, 0)
[explode_setup(df, columns = ['states'], delimiter = ';')] time=0:00:00.000466 n_obs=4, n_col=5 delta=(0, 0)
[explode(df, column = 'num', ignore_index = False)] time=0:00:00.003697 n_obs=7, n_col=5 delta=(+3, 0)
[explode(df, column = 'text', ignore_index = False)] time=0:00:00.002642 n_obs=15, n_col=5 delta=(+8, 0)
[explode(df, column = 'states', ignore_index = False)] time=0:00:00.002184 n_obs=33, n_col=5 delta=(+18, 0)
[drop_duplicates(df)] time=0:00:00.001671 n_obs=33, n_col=5 delta=(0, 0)
Out[7]: 
   aaa  myid  num text          states
0   10     1    1   aa         Wyoming
0   10     1    1   aa        Illinois
0   10     1    1   aa   New Hampshire
0   10     1    1   bb         Wyoming
0   10     1    1   bb        Illinois
0   10     1    1   bb   New Hampshire
0   10     1    1   cc         Wyoming
0   10     1    1   cc        Illinois
0   10     1    1   cc   New Hampshire
0   10     1    2   aa         Wyoming
0   10     1    2   aa        Illinois
0   10     1    2   aa   New Hampshire
0   10     1    2   bb         Wyoming
0   10     1    2   bb        Illinois
0   10     1    2   bb   New Hampshire
0   10     1    2   cc         Wyoming
0   10     1    2   cc        Illinois
0   10     1    2   cc   New Hampshire
0   10     1    3   aa         Wyoming
0   10     1    3   aa        Illinois
0   10     1    3   aa   New Hampshire
0   10     1    3   bb         Wyoming
0   10     1    3   bb        Illinois
0   10     1    3   bb   New Hampshire
0   10     1    3   cc         Wyoming
0   10     1    3   cc        Illinois
0   10     1    3   cc   New Hampshire
1   11     2  NaN  NaN    Pennsylvania
2   12     3    1   cc        New York
2   12     3    1   dd        New York
2   12     3    2   cc        New York
2   12     3    2   dd        New York
3   13     4  NaN   ee    Pennsylvania
```