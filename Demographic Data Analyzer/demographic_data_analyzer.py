import pandas as pd

DATA_PATH = "./adult.data.csv"
BACHELORS = "Bachelors"
EDUCATION = "education"
RACE = "race"
SEX = "sex"
MASTERS = "Masters"
DOCTORATE = "Doctorate"
HOURXWEEK = "hours-per-week"
SALARY = "salary"
NATIVE_COUNTRY = "native-country"


def calculate_demographic_data(print_data=True):
    df = pd.read_csv(DATA_PATH)
    r_count = df[RACE].value_counts()
    avg_age_m = round(df[df[SEX] == "Male"]["age"].mean(), 1)
    percent_bachelors = round(
        df[EDUCATION].value_counts()[BACHELORS] * 100 / df.shape[0], 1
    )
    hig_edu = df[
        (df[EDUCATION] == BACHELORS)
        | (df[EDUCATION] == MASTERS)
        | (df[EDUCATION] == DOCTORATE)
    ]
    low_edu = df[
        (df[EDUCATION] != BACHELORS)
        & (df[EDUCATION] != MASTERS)
        & (df[EDUCATION] != DOCTORATE)
    ]
    hig_edu_rich = round(
        hig_edu[hig_edu[SALARY] == ">50K"].shape[0] * 100 / hig_edu.shape[0], 1
    )
    low_edu_rich = round(
        low_edu[low_edu[SALARY] == ">50K"].shape[0] * 100 / low_edu.shape[0], 1
    )

    min_work_hours = df[HOURXWEEK].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df[HOURXWEEK] == min_work_hours]

    rich_percentage = (
        num_min_workers[num_min_workers[SALARY] == ">50K"].shape[0]
        * 100
        / num_min_workers.shape[0]
    )

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (
        (
            df[df[SALARY] == ">50K"][NATIVE_COUNTRY].value_counts()
            * 100
            / df[NATIVE_COUNTRY].value_counts()
        )
        .sort_values(ascending=False)
        .index[0]
    )
    highest_earning_country_percentage = round(
        (
            df[df[SALARY] == ">50K"][NATIVE_COUNTRY].value_counts()
            * 100
            / df[NATIVE_COUNTRY].value_counts()
        ).sort_values(ascending=False)[highest_earning_country],
        1,
    )

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df[df[SALARY] == ">50K"][df[df[SALARY] == ">50K"][NATIVE_COUNTRY] == "India"][
            "occupation"
        ]
        .value_counts()
        .index[0]
    )

    if print_data:
        print("Number of each race:\n", r_count)
        print("Average age of men:", avg_age_m)
        print(f"Percentage with Bachelors degrees: {percent_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {hig_edu_rich}%")
        print(f"Percentage without higher education that earn >50K: {low_edu_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": r_count,
        "average_age_men": avg_age_m,
        "percentage_bachelors": percent_bachelors,
        "higher_education_rich": hig_edu_rich,
        "lower_education_rich": low_edu_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
