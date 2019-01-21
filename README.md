# Hotel-Rate-Plan-Data
Models hotel rate plan production by metric over date set

A rough attempt at combining pulling data from CSV file, taking user input for data they wish to see, and displaying a line chart about the data using pygal. The program prompts a user to enter what rate plan they wish to see data about, prompts what kind of metric they wish to see displayed (room nights produced, average daily rate, revenue) and the date range for seeing the production. 

Using a series of try and except blocks to prompt users to input data they wish to see, and if it is not in the CSV file/incorrect format for searching, to reprompt for information again. 

A big component was allowing users to set a date range for the data about a rate plan they wished to be plotted, and correctly calculating the date delta between the start and end dates for the search. Unfortunately this is currently limited to dates in 2017, but program is able to detect and raise rror for re-prompting for dates if initially inputted date is out of range. 

Can certainly be refactored for less cluttered file, and working on adding more features and cleaning up plot display as axes can get cluttered easily and become illedgible once too many dates are selected.
