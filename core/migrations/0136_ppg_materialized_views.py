# Generated by Django 2.2 on 2024-05-29 19:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0135_match_enabled'),
    ]

    operations = [
        migrations.RunSQL(
            '''
-- Create a Materialized View for Points Per Game (PPG) by player
DROP MATERIALIZED VIEW IF EXISTS player_ppg;
CREATE MATERIALIZED VIEW IF NOT EXISTS player_ppg AS
SELECT
    p.id,
    p.import_id,
    p.full_name,
    SUM(me.points) / COUNT(me.match_id) AS ppg,  -- Calculate Points Per Game (PPG)
    -- CASE WHEN SUM(me.points) / COUNT(me.match_id) < 0 THEN 0 ELSE SUM(me.points) / COUNT(me.match_id) END AS ppg,  -- Calculate Points Per Game (PPG)
    SUM(CASE WHEN me.type = 45 THEN 1 ELSE 0 END) AS total_goals  -- Counting goals
    -- SUM(CASE WHEN me.type = 58 OR me.type = 59 THEN 1 ELSE 0 END) AS total_yellow_cards,  -- Counting yellow_cards
    -- SUM(CASE WHEN me.type = 60 THEN 1 ELSE 0 END) AS total_red_cards  -- Counting red_cards
FROM
    match_events me
JOIN players p ON p.id = me.player_id
WHERE
    points IS NOT NULL  -- Consider only events with non-null points
GROUP BY
    p.id
ORDER BY
    ppg DESC;
REFRESH MATERIALIZED VIEW player_ppg;

-- Create a function to refresh the materialized view
CREATE OR REPLACE FUNCTION refresh_player_ppg_view()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if the new status is 'e' and it is different from the old status
    IF NEW.status = 'e' AND OLD.status IS DISTINCT FROM NEW.status THEN
        -- Refresh the materialized view
        PERFORM pg_sleep(2);  -- Add a slight delay to ensure all related changes are committed
        REFRESH MATERIALIZED VIEW player_ppg;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger on the matches table to call the function when the status changes to 'e'
CREATE OR REPLACE TRIGGER match_end_refresh_ppg
AFTER UPDATE OF status ON matches
FOR EACH ROW
WHEN (NEW.status = 'e' AND OLD.status IS DISTINCT FROM NEW.status)
EXECUTE FUNCTION refresh_player_ppg_view();
''',
'''
DROP MATERIALIZED VIEW IF EXISTS player_ppg;
DROP FUNCTION IF EXISTS refresh_player_ppg_view;
DROP TRIGGER IF EXISTS match_end_refresh_ppg ON matches;
''',
        )
    ]
