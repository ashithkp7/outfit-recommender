
from recommender.outfit_recommender import OutfitRecommender

def main():
  recommender = OutfitRecommender("data/outfits.csv")
  print("Recommendations for color='Blue', occasion='Casual':")
  print(recommender.recommend(color='Blue', occasion='Casual'))

if __name__ == "__main__":
  main()
