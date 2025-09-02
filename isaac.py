import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class ECDF:
    def __init__(self, data):
        self.data = sorted(data)

    def compute_ecdf(self, x):
        return sum(1 for i in self.data if i <= x) / len(self.data)

    def compute_quantile(self, q):
        if q < 0 or q > 1:
            raise ValueError("Quantile must be between 0 and 1")
        index = q * (len(self.data) - 1)
        if index.is_integer():
            return self.data[int(index)]
        else:
            lower_index = int(index)
            return (self.data[lower_index] + self.data[lower_index + 1]) / 2

    def compute_iqr(self):
        q1 = self.compute_quantile(0.25)
        q3 = self.compute_quantile(0.75)
        return q3 - q1

    def compute_whiskers(self):
        iqr = self.compute_iqr()
        q1 = self.compute_quantile(0.25)
        q3 = self.compute_quantile(0.75)
        lower_whisker = q1 - 1.5 * iqr
        upper_whisker = q3 + 1.5 * iqr
        return lower_whisker, upper_whisker

    def compute_five_number_summary(self):
        lower_whisker, upper_whisker = self.compute_whiskers()
        min_val = min(self.data)
        max_val = max(self.data)
        median = self.compute_quantile(0.5)
        iqr = self.compute_iqr()
        return lower_whisker, min_val, median, max_val, upper_whisker, iqr

    def is_outlier(self):
        lower_whisker, upper_whisker = self.compute_whiskers()
        return [x < lower_whisker or x > upper_whisker for x in self.data]


# Example usage
ecdf = ECDF(df['Age at Diagnosis'])

print(ecdf.compute_five_number_summary())
print(ecdf.is_outlier())

sns.boxplot(ecdf.data)
plt.show()
