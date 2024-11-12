# Did Trump's conspiracy theories really entertain YouTube?

---

## Abstract
To investigate whether videos about Trump's conspiracy theories can get more likes on YouTube.

## Methods
First, we filter the YouTube dataset for entries that contain the keyword "Trump," while limiting the scope to the entertainment category. Then, we will divide the dataset into two groups: videos containing keywords related to Trump's conspiracy theories as the treated group, and the remaining videos as the control group for comparative analysis.

In addition to the presence of conspiracy theories, factors such as video length, view count, and others may also influence the number of likes. Therefore, we plan to use logistic regression to calculate the propensity score and match data with similar propensity scores to create a control group for comparison. Finally, we will use visualizations and t-tests to validate our hypothesis.

## Proposed additional datasets
When processing the data, we noticed that the number of subscribers to a channel may be an important factor influencing the number of likes on a video. However, the current dataset we are using does not include this feature. Therefore, we might consider using another dataset from this repository to perform a join operation. This way, when we use propensity scores to balance the data, we may achieve more convincing results.