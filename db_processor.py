import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# [DB] articles 테이블 insert
def insert_into_articles(article):
    response = (
        supabase.table('articles').insert({
            "title": article["title"],
            "link": article["link"]
        }).execute()
    )
    
    inserted_row = response.data[0] 
    generated_uuid = inserted_row['id'] 

    return generated_uuid