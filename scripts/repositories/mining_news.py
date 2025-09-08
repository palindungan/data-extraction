class MiningNews:
    @staticmethod
    def get_data(
            cursor=None,
            select='mining_news.*',

            get_by_id=None,
            get_by_code=None,
    ):
        where_id = ''
        if get_by_id is not None:
            where_id = f"""
                AND mining_news.id = %(get_by_id)s
            """

        where_code = ''
        if get_by_code is not None:
            where_code = f"""
                AND mining_news.code = %(get_by_code)s
            """

        query = f"""
            SELECT
                {select}
            FROM
                mining_news
            WHERE
                mining_news.id != 0
                {where_id}
                {where_code}
        """

        cursor.execute(query, ({
            'get_by_id': get_by_id,
            'get_by_code': get_by_code,
        }))

        return cursor

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

        title = data['title']
        url = data['url']
        date = data['date']
        description = data['description']
        site_name = data['site_name']
        site_base_url = data['site_base_url']

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

                            title,
                            url,
                            date,
                            description,
                            site_name,
                            site_base_url,

                            created_at,
                            updated_at
                        )
                    VALUES
                        (
                            %(mining_source_id)s,
                            %(code)s,
                            %(data)s,

                            %(title)s,
                            %(url)s,
                            %(date)s,
                            %(description)s,
                            %(site_name)s,
                            %(site_base_url)s,

                            now(),
                            now()
                        )
                    RETURNING *
                """
                cursor.execute(query, ({
                    'mining_source_id': mining_source_id,
                    'code': code,
                    'data': data,

                    'title': title,
                    'url': url,
                    'date': date,
                    'description': description,
                    'site_name': site_name,
                    'site_base_url': site_base_url,
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
        import os
        import psycopg2
        from psycopg2 import extras
        from dotenv import load_dotenv

        load_dotenv()
        db_url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(db_url)

        with connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
                cursor_result = MiningNews.get_data(
                    cursor=cursor,
                    select=f"""
                        mining_news.*
                    """,
                    get_by_code=code,
                )
                mining_news = cursor_result.fetchone()
                if mining_news:
                    MiningNews.update(
                        mining_source_id=mining_source_id,
                        code=code,
                        data=data,
                    )
                else:
                    MiningNews.store(
                        mining_source_id=mining_source_id,
                        code=code,
                        data=data,
                    )
