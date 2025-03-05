\set pguser `echo "$POSTGRES_SUPABASE_USER"`

CREATE DATABASE _supabase WITH OWNER :pguser;
