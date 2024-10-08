# CR(Company Review)_Project
We started this project because we wanted to improve the organizational culture and satisfaction of employees by using generative AI to utilize external and internal data together. 
We collected data from 60000+ major LG subsidiaries (Display, Electronics, Life Health, etc.) through data crawling from blind/job planet sites.

We built a data classification model for company review data using human annotation + GPT annotation (fine-tuning, in-context learning). (Baseline) GPT-4o mini : 81% accuracy → fine-tune GPT-4o mini : 92% accuracy, (Baseline) GPT-4o : 76% accuracy → fine-tune GPT-4o 94% accuracy

We succeeded in achieving higher performance than the baseline. After that, we proceeded to analyze companies through KOME (moral sentiment) + company review data classification model to derive insights.
