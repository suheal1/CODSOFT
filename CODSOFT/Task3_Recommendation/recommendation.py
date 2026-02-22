import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Make titles lowercase for flexible search
movies["title"] = movies["title"].str.lower()

# Convert genre text into numeric vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

# Compute similarity matrix
similarity = cosine_similarity(genre_matrix)

def recommend(movie_title):
    movie_title = movie_title.lower()

    if movie_title not in movies["title"].values:
        print("Movie not found in database.")
        return

    movie_index = movies[movies["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[movie_index]))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nMovies similar to '{movie_title.title()}':\n")

    count = 0
    for i in sorted_scores[1:]:
        print("-", movies.iloc[i[0]]["title"].title())
        count += 1
        if count == 3:
            break

def main():
    print("🎬 Movie Recommendation System")
    print("Type 'exit' to quit\n")

    while True:
        movie = input("Enter a movie name: ")

        if movie.lower() == "exit":
            print("Goodbye!")
            break

        recommend(movie)
        print()

if __name__ == "__main__":
    main()