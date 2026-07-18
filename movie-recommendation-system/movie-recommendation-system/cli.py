"""Simple command-line interface for the Movie Recommender."""

from recommender import MovieRecommender


def main():
    engine = MovieRecommender()

    print("=" * 50)
    print(" MOVIE RECOMMENDATION SYSTEM (CLI)")
    print("=" * 50)
    print("\nAvailable movies:")
    for t in engine.get_all_titles():
        print(f"  - {t}")

    while True:
        print("\n" + "-" * 50)
        title = input("Enter a movie title (or 'exit' to quit): ").strip()
        if title.lower() == "exit":
            break

        results = engine.recommend(title, top_n=5)
        if results is None:
            print("Movie not found. Please check the spelling / list above.")
            continue

        print(f"\nBecause you liked '{title}', you might also like:\n")
        for r in results:
            print(f"  {r['title']}  (similarity: {r['similarity']})")
            print(f"    Genres: {r['genres']}")
            print(f"    {r['overview']}\n")


if __name__ == "__main__":
    main()
