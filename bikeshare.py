import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Please enter the city(chicago, new york city, washington) you want to analyze:")
        if city.lower() in ['chicago', 'new york city', 'washington']:
            print('You selected {} for analysis'.format(city))
            break
        else:
            print('not a valid city name please choose from chicago, new york city and washington')

    while True:
        month = input("Please enter a month (all, january, february, ... , june) you want to analyze:")
        if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('You selected {} for analysis'.format(month))
            break
        else:
            print('not a valid month, please choose from the list above')

    while True:
        day = input("Please enter a weekday (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) you want to analyze:")
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            print('You selected {} for analysis'.format(day))
            break
        else:
            print('not a valid month, please choose from the list above')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    city = city.lower()
    month = month.lower()
    day = day.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january' , 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    print('The most common month is {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is {}'.format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    df['comb'] = df['Start Station'] + ' And ' + df['End Station']
    # TO DO: display most commonly used start station
    print('The most common start station is {}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('The most common end statation is {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most common combination of start and end station is {}'.format(df['comb'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Average travel time is {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of each user types is\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('The Counts of gender is\n',df['Gender'].value_counts())
    except:
        print('Gender info is not available for selected city')
            # TO DO: Display earliest, most recent, and most common year of birth

    try:
        print('The earliest, most recent and most common year of birth are respectively {},{} and {}'.format(int(df['Birth Year'].min()),int(df['Birth Year'].mode()[0]),int(df['Birth Year'].max())))
    except:
        print('Birth Year info is not available for selected city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        count = 0
        while True:
            raw = input('\nWould you like to see the raw data? Enter yes or no.\n')

            if raw.lower() == 'yes':
                print(df.iloc[count:count+5])
                count = count + 5
            else:
                break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
