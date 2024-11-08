# ADA Project Milestone 2

## Why Trump Embraces Conspiracy Theories: A Deep Dive into YouTube’s Role in Amplifying Controversy and Captivating Audiences

### Abstract
This study explores how Donald Trump uses conspiracy theories to capture attention on YouTube. Analyzing millions of videos, we reveal that conspiracy content drives higher engagement and trace how these narratives spread, often amplified by both mainstream and alternative channels. Our findings highlight how conspiracy theories become powerful tools for emotional engagement, illustrating YouTube’s role in amplifying political influence.

### 1. 阴谋论传播的时间序列分析

- **研究问题**：特朗普是如何利用阴谋论在YouTube上获得关注？阴谋论相关内容的传播轨迹如何？
- **技术手段**：
  - **筛选**：通过标题、描述和标签中出现的阴谋论相关词（如"QAnon"、"Deep State"等）提取相关视频。
  - **时间序列分析**：使用时间序列模型，分析这些视频随时间变化的发布频率、观看量和互动量。
  - **关联事件分析**：将数据与真实事件时间线（如选举、弹劾事件）相结合，观察阴谋论内容的发布和观看峰值。
- **预期结果**：展示阴谋论内容的发布和传播规律，以及这些内容如何在事件发生时获得关注，比如是否是关键的竞选节点等等

### 2. 阴谋论 vs. 非阴谋论内容的互动比较

- **研究问题**：包含阴谋论内容的视频是否比普通视频获得更多的关注（点赞、点踩、观看量等）？
- **技术手段**：
  - **筛选**：通过标题、描述和标签中出现的阴谋论相关词（如"QAnon"、"Deep State"等）提取相关视频
  - **分组比较**：将视频分为“阴谋论”和“非阴谋论”两组，分析两组之间的点赞数、点踩数、观看量的差异
  - **统计测试**：判断两组之间的互动差异是否具有统计显著性
- **预期结果**：通过比较分析，展示阴谋论相关内容是否在互动上有更高的吸引力，解释阴谋论在社交媒体上如何引起注意

### 3. 社交媒体上的阴谋论传播路径与内容放大效应

- **研究问题**：YouTube上的阴谋论内容如何逐渐被自媒体放大？主流媒体与自媒体在阴谋论内容传播中的关系如何？
- **技术手段**：
  - **传播网络分析**：基于发布阴谋论相关内容的频道，构建传播网络，分析不同频道间的互动和内容扩散路径
  - **信息流分析**：追踪从主流媒体（如官方新闻频道）到自媒体（如个人频道）的视频传播路径，观察阴谋论话题的放大过程
  - **社区检测**：使用社区检测算法（如Louvain算法），识别在传播阴谋论内容上具有较强联系的频道群体，分析这类视频的特征和互动关系
- **预期结果**：分析出来阴谋论内容在YouTube上的传播路径和扩散模式，从而能解释平台上的内容放大机制

### 4. 特朗普相关视频的娱乐化倾向分析

- **研究问题**：哪些频道以娱乐的方式制作特朗普视频？娱乐化内容是否吸引更多观看？
- **技术手段**：
  - **内容分类**：根据视频标题、描述和标签，可能使用文本分类模型（如TF-IDF + KNN）识别“娱乐化”内容。
  - **观众行为分析**：比较娱乐化视频与非娱乐化视频的观看次数、平均观看时长和互动量，分析娱乐化倾向对观众行为的影响。
  - **趋势分析**：考察娱乐化内容在不同事件时期的变化趋势，观察娱乐化内容是否在特定时期（如选举期间）增加。
- **预期结果**：展示娱乐化内容在特朗普相关视频中的占比及其观众偏好，解释娱乐化对政治话题传播的影响

### 5. 阴谋论和娱乐内容的交叉影响

- **研究问题**：包含阴谋论和娱乐标签的视频是否更容易在社交媒体上广泛传播？
- **技术手段**：
  - **双标签分析**：筛选包含“阴谋论”和“娱乐”标签的视频，分析其观看次数、互动量和传播速度。
  - **内容组合效应分析**：比较阴谋论、娱乐和两者组合的内容在传播速度和观众互动上的差异。
  - **机器学习模型**：使用机器学习模型（如随机森林或逻辑回归）预测带有两者组合的内容的互动量，以衡量阴谋论和娱乐标签组合的效果。
- **预期结果**：分析阴谋论与娱乐化内容的组合是否会增加视频的传播力度，也就是说“乐子人”也助长了此类话题的传播

---

### Conclusion

This study reveals that Donald Trump’s embrace of conspiracy theories plays a strategic role in capturing public attention and cultivating a powerful persona. By positioning himself as a “fighter against the establishment,” Trump taps into narratives that resonate emotionally with audiences, casting himself as a rebellious figure challenging unseen forces. This framing, coupled with the amplification effects of video platforms like YouTube, has proven remarkably effective in drawing engagement and strengthening his following. Our analysis shows that conspiracy-themed content consistently drives higher interaction, as viewers are drawn into sensationalized stories that feel urgent and provocative. Ultimately, this research underscores how Trump’s affinity for conspiracy-laden discourse, reinforced by digital media dynamics, amplifies his influence and creates a compelling spectacle that captivates millions.