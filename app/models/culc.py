import pandas as pd
import app.lib.log as log

logger = log.getLogger(__name__)


def count_by_column(data, column):
    df = pd.DataFrame(data)
    if column not in df.columns:
        logger.error('column "%s" not exists', column)
        return []

    sum = df[column].value_counts().to_dict()
    results = list(map(lambda k: {column: k, 'count': sum[k]}, sum.keys()))
    return results


def pivot_count_by_columns(data, index, column):
    df = pd.DataFrame(data)

    table = pd.pivot_table(df, index=index, columns=column, aggfunc=len)

    if column not in df.columns:
        logger.error('column "%s" not exists', column)
        return []

    sum = df[column].value_counts().to_dict()
    results = list(map(lambda k: {column: k, 'count': sum[k]}, sum.keys()))
    return results
