\set pguser `echo "$POSTGRES_SUPABASE_USER"`

create schema if not exists _realtime;
alter schema _realtime owner to :pguser;
