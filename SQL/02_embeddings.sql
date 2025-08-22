-- Add embedding columns
ALTER TABLE employees ADD COLUMN IF NOT EXISTS name_embedding vector(1536);
ALTER TABLE orders ADD COLUMN IF NOT EXISTS customer_name_embedding vector(1536);
ALTER TABLE products ADD COLUMN IF NOT EXISTS name_embedding vector(1536);
