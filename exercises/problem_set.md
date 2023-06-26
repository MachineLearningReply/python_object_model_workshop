# Problem Set: Python Object Model Workshop 

Your cinema, called Apollo, is a success! Despite a few setbacks, your strong coding abilities, expertise in testing Python code, and analytical mindset enabled you to improve your customer satisfaction. Of course, your excellent taste in movies played a role as well. 

As a cinema owner, your next step is to open a chain of Apollo theatres, starting with Apollo I. But to ensure the success of Apollo II, you plan to create a data-driven recommender model that suggests movies based on customer preferences. To achieve this, you must gather data by building a proof of concept for a movie database that stores metadata and ratings.

1. Define an abstract class for movies. Furthermore, define getter and setter methods for the `title`, `description`, `length`, `genre` & `rating`.
2. You may need to print the movie to the console for debugging. In that case, you want to see the following information: `title`, `genre`, `length` & `description`
3. For now, create an empty class called `CinemaMovie` that inherits from your abstract movie class.
4. Create a class called `MovieDB` that initializes with an empty list called `movies`. 
5. Add a class method called `from_csv` to initialize a `MovieDB` object by reading a CSV file. `from_csv` needs to fulfill the following requirements:
	- Uses a context manager to read the file
	- Instantiates a `CinemaMovie` object for each movie and adds it to `movies`.
6. Tie everything together by reading `movies.csv` and printing each `CinemaMovie` object to the console. Keep in mind of using `if __name__ == "__main__":`.