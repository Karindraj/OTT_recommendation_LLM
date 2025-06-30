
MODEL_NAME = "mistral"  # Ollama model for answer generation
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # switched from nomic-embed-text
VECTOR_DB_PATH = "index"

DATA_FILES = {
    "catalog": "data/Updated_Synthetic_Dataset__500_Rows_.csv",
    "preferences": "data/User_Preference_Profiles.csv",
    "metadata": "data/synthetic_dataset_metadata.csv"
}

NEO4J_CONFIG = {
    "uri": "bolt://localhost:7687",
    "user": "neo4j",
    "password": "password"
}

RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"