# Task_04_Descriptive_Stats

## Instructions to Run the Code

1. **Clone this repository** and add the dataset files (`2024_fb_ads_president_scored_anon.csv`, `2024_fb_posts_president_scored_anon.csv`, `2024_tw_posts_president_scored_anon.csv`) to the project folder.  
   _**Note:** Datasets are not included for privacy._

2. **Install dependencies** (for Pandas/Polars scripts):
    ```sh
    pip install pandas polars
    ```

3. **Run the scripts** for each approach and dataset:

    - **Pure Python:**
      ```sh
      python pure_python_stats/pure_python_stats_2024_fb_ads_president_scored_anon.py
      python pure_python_stats/pure_python_stats_2024_fb_posts_president_scored_anon.py
      python pure_python_stats/pure_python_stats_2024_tw_posts_president_scored_anon.py
      ```

    - **Pandas:**
      ```sh
      python pandas_stats/pandas_stats_2024_fb_ads_president_scored_anon.py
      python pandas_stats/pandas_stats_2024_fb_posts_president_scored_anon.py
      python pandas_stats/pandas_stats_2024_tw_posts_president_scored_anon.py
      ```

    - **Polars:**
      ```sh
      python polars_stats/polars_stats_2024_fb_ads_president_scored_anon.py
      python polars_stats/polars_stats_2024_fb_posts_president_scored_anon.py
      python polars_stats/polars_stats_2024_tw_posts_president_scored_anon.py
      ```

4. **Outputs** will be printed to the console.  
   To save output, use:
   ```sh
   python pandas_stats/pandas_stats_2024_fb_posts_president_scored_anon.py > fb_post_stats.txt



## Summary of Findings & Insights

- **Numeric engagement fields** (e.g., Likes, Comments, Shares) are highly skewed: a small number of posts/tweets drive most interactions.

- **Content and topic indicator columns** (like `attack_msg_type_illuminating`, `covid_topic_illuminating`) are mostly zeros, showing that most posts/tweets do not focus on these topics.

- **Dominant categories:** The majority of Facebook pages are US-based and categorized as `PERSON`.

- **Grouping:** For Facebook Posts, statistics by `Facebook_Id` (page) and `post_id` (post) provide deeper insights into page-level and post-level activity.

- **No user_id in Twitter data:** Grouped analysis is performed by available fields like `lang` (language) and `month_year`.

- **Performance:** Pandas and Polars scripts run much faster and are easier to extend compared to pure Python.

