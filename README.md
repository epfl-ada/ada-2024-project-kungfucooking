## Dataset Information for Milestone 2

In Milestone 2, we use the **YouNiverse** dataset. Due to the large size of these files, they are not included in this repository. However, for accurate execution of the analysis, they should be placed in the main folder of this repository, at the same level as the Jupyter Notebook files.

- `df_channels_en.tsv`
- `df_timeseries_en.tsv.gz`
- `yt_metadata_en.jsonl.gz`

The `yt_metadata_en.jsonl.gz` file is processed through `data_preprocess.py`, resulting in a filtered dataset used in this milestone, named `yt_metadata_filtered_"trump ".jsonl`.

The **YouNiverse** dataset provides a highly diverse and rich collection of data, offering extensive possibilities for in-depth analysis and insights. Its comprehensive nature allows for a wide range of analytical approaches and interpretations, making it ideal for advanced exploration.

We also have the necessary hardware and software resources to effectively process and interpret this dataset. Our setup ensures efficient handling of large-scale data, allowing us to leverage the full potential of the YouNiverse dataset in our analysis.

---

# Why Donald Trump Embraces Conspiracy Theories: A Deep Dive into YouTube’s Role in Amplifying Controversy and Captivating Audiences

---

## Abstract

This study aims to explore the impact of the conspiracy theories proposed by Donald Trump on YouTube. Analyzing millions of videos, we reveal that conspiracy content drives higher engagement and trace how these narratives spread, often amplified by both mainstream and alternative channels. Our findings highlight how conspiracy theories become powerful tools for emotional engagement, illustrating YouTube’s role in amplifying political influence.

## Research Questions
- How did Trump use conspiracy theories to gain attention on YouTube? What is the trajectory of the dissemination of conspiracy theory-related content?
- Do videos containing conspiracy theory content attract greater attention (e.g., likes, dislikes, views) compared to videos without conspiracy theory keywords?
- Is there the trend of channels creating Trump-related videos with an entertainment focus generates higher view counts? And what are the subscription differences before and after a video publishing?
- How do the presence of conspiracy theory keywords in the title or tags and whether the video belongs to the entertainment category interactively influence the number of likes a video receives?

## Project Plans & Methods

### Task 1: Time Series Analysis of Conspiracy Propagation

Relevant videos were initially filtered using keywords related to conspiracy theories, such as "QAnon" and "Deep State",  found in the `titles`, `descriptions`, or `tags`. To control for variables, we categorized the videos and identified the top four categories representing approximately 90% of the content. This approach also allowed us to exclude clearly irrelevant categories, such as "Autos & Vehicles". Time series analysis was then conducted to examine trends in posting frequency, views, and interactions over time. To minimize short-term fluctuations, we aggregated the data monthly, enabling us to observe overall trends. Additionally, the data was normalized, allowing us to compare changes in views, subscriptions, and video uploads per unit of time on a single graph without distorting trends.

### Task 2: Comparative Analysis of Videos Containing Conspiracy Terms vs. Non-Conspiracy Content

After filtering relevant videos using the method mentioned above, we categorize the videos into two groups: "Conspiracy Theory" and "Non-Conspiracy Theory", to perform a comparative analysis of engagement metrics, such as likes, dislikes, like-to-dislike ratio, view count-to-video count ratio, likes-to-video count ratio, total view counts and others. Statistical analyses will be conducted to assess whether the observed interaction differences between the two groups were statistically significant.we will perform a causal analysis, isolating and controlling for variables like subscriber counts and content type. This can help us obtain a clearer understanding of the unique impact of conspiracy-related content on engagement metrics.

### Task 3: Tracing the Sequential Pathways of Trump-Related Conspiracy Theories on YouTube

We began by filtering Trump-related YouTube videos, isolating those containing five specific conspiracy keywords. A time-series analysis of these videos revealed two primary peaks in content volume: October 2018, coinciding with the U.S. midterm elections, and November 2019, aligning with the start of impeachment discussions. Given the significance of these periods, we focused our analysis on them, selecting three major channel categories —- *News & Politics*, *People & Blogs*, and *Entertainment*. To examine the dissemination pattern across these channels, we employed convolution and normalization techniques to calculate the relative time lags in content release. Cross-correlation analysis allowed us to establish the temporal order of content publication, revealing that conspiracy content typically first appeared in *People & Blogs*, followed by *News & Politics*, and lastly in *Entertainment*. This sequence suggests a path of initial public response, subsequent journalistic coverage, and eventual entertainment adaptation, highlighting the dynamics of conspiracy theory spread across different channel types.

### Task 4: Analysis of the Entertainment Inclination in Trump-Related Videos

First, we will identify Trump-related videos in the entertainment category and compare them with non-entertainment videos to see if there is a significant difference in like rates. The like rate will be calculated as `(like_count - dislike_count * 0.5) / view_count`. Additionally, we have identified a specific channel within the entertainment category that has produced over 10,000 videos, and we intend to conduct a detailed analysis of this channel to examine if the entertainment focus contributes to greater engagement and higher returns.

Lastly, we will select a group of channels with similar characteristics and analyze time series data around the release of these entertainment videos. By performing linear regression on view counts or subscription counts before and after video releases, we will examine if there is a notable difference in the slope, indicating the video's impact. Furthermore, we aim to assess whether the influence of entertainment videos differs from that of non-entertainment videos in this context.

### Task 5: Exploring the Intersection of Conspiracy Theories and Entertainment Content

Through a comprehensive analysis, we observed that videos related to Trump in the entertainment category tend to have more views and likes compared to those in the news and politics category. We aim to explore whether videos that include conspiracy theory keywords in their titles or tags and belong to the entertainment category can receive more likes. First, we plan to calculate the propensity score using logistic regression, balancing the data (such as view count, video duration, channel subscriptions, etc.) by matching the propensity scores. We will observe the results under the combination of the presence of keywords and belonging to the entertainment category, visually presenting the data and validating it through t-tests. Additionally, we plan to conduct an in-depth analysis of specific cases (such as studying only a few specific channels) to observe how the two factors jointly influence the outcomes.

## Timeline
- [x] 15.11.2024 Data Handling and Preprocessing & Initial Exploratory Data Analysis

- [ ] 30.11.2024 Task1-5 Implementation and Preliminary Analysis

- [ ] 07.12.2024 Compile Final Analysis

- [ ] 14.12.2024 Report Writing

- [ ] 20.12.2024 Milestone 3 Deadline

## Team Organization
- Yuheng: Task 1
- Yifan: Task 2
- Yejie: Task 3
- Tianshuo: Task 4
- Yixiang: Task 5

Each team member will be responsible for creating the final visualizations for their respective task, completing the data story.






