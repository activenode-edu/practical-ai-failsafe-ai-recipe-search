DROP FUNCTION IF EXISTS match_recipes;
create or replace function match_recipes (
  query_embedding vector(768),
  match_threshold float,
  match_count int
)
returns table (
  id bigint,
  content text,
  title text,
  similarity float
)
language sql stable
as $$
  select
    recipes.id,
    recipes.content,
    recipes.title,
    1 - (recipes.embedding <=> query_embedding) as similarity
  from recipes
  where recipes.embedding <=> query_embedding < 1 - match_threshold
  order by recipes.embedding <=> query_embedding
  limit match_count;
$$;
