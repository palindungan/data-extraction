class MiningNews:
    @staticmethod
    def store(
            mining_source_id=None,
            code=None,
            data=None,
    ):
        import os
        import json
        import psycopg2
        from psycopg2 import extras
        from dotenv import load_dotenv

        load_dotenv()
        db_url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(db_url)

        if data:
            data = json.dumps(data)

        with connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
                query = f"""
                    INSERT INTO mining_news
                        (
                            mining_source_id,
                            code,
                            data,

                            created_at,
                            updated_at
                        )
                    VALUES
                        (
                            %(mining_source_id)s,
                            %(code)s,
                            %(data)s,

                            now(),
                            now()
                        )
                    RETURNING *
                """
                cursor.execute(query, ({
                    'mining_source_id': mining_source_id,
                    'code': code,
                    'data': data,
                }))
                connection.commit()
                result = cursor.fetchone()

        return result

    @staticmethod
    def update(
            mining_source_id=None,
            code=None,
            data=None,
    ):
        import os
        import json
        import psycopg2
        from psycopg2 import extras
        from dotenv import load_dotenv

        load_dotenv()
        db_url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(db_url)

        if data:
            data = json.dumps(data)

        with connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
                query = f"""
                    UPDATE mining_news
                    SET
                        mining_source_id = %(mining_source_id)s,
                        code = %(code)s,
                        data = %(data)s,

                        updated_at = now()
                    WHERE
                        code = %(code)s
                    RETURNING *
                """
                cursor.execute(query, ({
                    'mining_source_id': mining_source_id,
                    'code': code,
                    'data': data,
                }))
                connection.commit()
                result = cursor.fetchone()

        return result

    @staticmethod
    def auto_update(
            mining_source_id=None,
            code=None,
            data=None,
    ):
        pass
